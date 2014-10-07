#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Optimizador de asignacion de CUPOS

Authors: Grupo MisoAgiles 2014
"""

import psycopg2

from pulp import *

class AsignadorCupos:
    #Declaracion de variables de la clase
    totalestudiantes = 0
    totalmaterias = 0
    ESTUDIANTES = []
    CURSOS = []
    SECCIONES = []
    HORARIOS = []

#SEC_X_CUR[i] retorna k: La sección i es del curso k
    SEC_X_CUR = {}

    #SEC_X_HOR[i] retorna h: La sección i se dicta el día de la semana h
    SEC_X_HOR = {}

    # CUPOS[i] retorna c: La sección i tiene un cupo máximo de c estudiantes
    CUPOS = {}

    # EST_X_CUR[i][j] = 1, Si el estudiante i desea tomar el curso j
    #                 = 0, si el estudiante i no desea tomar el curso j
    EST_X_CUR = [[0 for i in range(4)] for i in range(5)]

    def __init__(self):
        print("Creacion")


    #################################################################################
    #
    # Poblar el arreglo de ESTUDIANTES y los cursos que desean tomar en los próximos
    # semestres
    #
    def poblar_estudiantesBD(self):
        #TODO Aqui se debe conectar a la base de datos y leer la información correspondiente a ESTUDIANTE y a
        #Obtiene la conexion
        try:
            conn = psycopg2.connect("dbname='d8iv5ac7d1jos6' user='kpbaqcwlfpqkgw' host='ec2-23-23-183-5.compute-1.amazonaws.com' password='4KLEgGfQDTQN2qgVYUo6DJfXiy'")

        except Exception:
            print("Fallo la conexion a la base de datos")

        #Crea los cursores para la ejecucion de las consultas
        curEstudiantes = conn.cursor()
        curCursos = conn.cursor()
        curSecciones = conn.cursor()
        curEstudiCur = conn.cursor()

        try:
            totalestudiantes = 0
            curEstudiantes.execute("SELECT id from siscupos_estudiante")
            rowsEstudiantes = curEstudiantes.fetchall()
            for rowE in rowsEstudiantes:
               self.ESTUDIANTES.append(rowE[0] - 9000)
               totalestudiantes = totalestudiantes + 1

            totalmaterias = 0
            curCursos.execute("SELECT id from siscupos_asignatura")
            rowsCursos = curCursos.fetchall()
            for rowC in rowsCursos:
               self.CURSOS.append(rowC[0] - 9000)
               totalmaterias = totalmaterias + 1


            #El siguiente query aplica pues solo se tiene un programa academico, en la siguiente version del optimizador
            #se deben tener en cuenta los programas => se debe modificar el query
            print("Ejecutar query de secciones")
            rowsSecciones = curSecciones.fetchall()
            curSecciones.execute(' select axp.asignatura_id curso '
                                 '      ,prp.id                  '
                                 '      ,prp.cupos cupos         '
                                 '      ,prp.diaSemana           '
                                 ' from siscupos_asignaturaxprograma axp '
                                 '    , siscupos_preprogramacion prp '
                                 ' where prp."asignaturaXPrograma_id" = axp.id'
            )
            for rowP in rowsSecciones:
               self.SEC_X_CUR[rowP[1]] = rowP[0] - 9000
               self.SEC_X_HOR[rowP[1]] = rowP[3]
               self.CUPOS[rowP[1]] = rowP[2]
               self.SECCIONES.append(rowP[1])


            print("Ejecutar query de deseadas")
            curEstudiCur.execute(
                             " select axe.asignatura_id curso "
                             "     , axe.estudiante_id estudiante "
                             "     , a.creditos_prerequisitos creditos_prerequisitos "
                             "    , ( "
                             "        select sum(a1.creditos) "
                             "        from siscupos_asignaturaxestudiante axe1 "
                             "            ,siscupos_asignatura a1 "
                             "        where axe1.asignatura_id = a1.id "
                             "        and axe1.cursada = 'S' "
                             "        and axe.estudiante_id = axe1.estudiante_id "
                             "       ) creditos_tomados "
                             " from siscupos_asignaturaxestudiante axe "
                             "    ,siscupos_asignatura a "
                             " where axe.asignatura_id = a.id "
                             " and axe.cursada = 'N' "
            )
            rowsEstudiCur = curEstudiCur.fetchall()
            self.EST_X_CUR = [[0 for i in range(totalmaterias+1)] for i in range(totalestudiantes+1)]
            #inicializa los valores en 0
            for x in range (1, totalestudiantes+1):
               for y in range (1, totalmaterias+1):
                  self.EST_X_CUR[x][y] = 0

           #actualiza los cursos deseados
            for rowEC in rowsEstudiCur:
               self.EST_X_CUR[rowEC[1]-9000][rowEC[0]-9000] = self.calcularPrioridad(rowEC[2], rowEC[3])


        except Exception as e:
            print("Error ejecutando el query ", e.message)

        return 1


    #################################################################################
    # Método que realiza la optimación de asignación de cupos en los cursos siguiendo
    # un algoritmo de programación linea.
    #
    def asignacion_optima(self):
        # Creacion del modelo

        prob = LpProblem("AsignacionCursos", LpMaximize)

        # asig_est corresponde a la variable donde se almacenará el resultado optimizado.
        #   asig_est(i,j) = 1, si el estudiante i es asignado al curso j
        #                 = 0, si el estudiante i no es asignado al curso j
        asig_est = LpVariable.dicts("AsigSugerida",
                                    [(i,j) for i in self.ESTUDIANTES
                                              for j in self.SECCIONES], 0, 1, LpBinary)

        #Inicialir asig_est
        for i in self.ESTUDIANTES:
            for j in self.SECCIONES:
              asig_est[(i,j)].varValue = 0

        ######################################################################################
        # Funcion objetivo: Maximizar el total de cupos asignados.
        #
        prob += lpSum(asig_est[(i,j)] for i in self.ESTUDIANTES for j in self.SECCIONES), "TotalAsignaciones"

        ######################################################################################
        # Restricciones del modelo de optinización
        #

        # Restriccion A: Un estudiante tiene un maximo de 2 cursos
        for i in self.ESTUDIANTES:
            labelA = "maxCur_%d" % i
            prob += lpSum(asig_est[(i,j)] for j in self.SECCIONES) <= 2, labelA

        # Restriccion B: Un estudiante no puede ser asignado a dos o más secciones del mismo curso
        for i in self.ESTUDIANTES:
            for j in self.SECCIONES:
                 prob += (lpSum(asig_est[(i, m)] for m in self.SECCIONES if m != j and self.SEC_X_CUR[m] == self.SEC_X_CUR[j] ) +
                          lpSum(asig_est[(i, j)] for m in self.SECCIONES if m == j ) <= 1)

        # Restriccion C: La asignacion a una sección no puede superar su cupo maximo
        for j in self.SECCIONES:
            labelB = "maxCupos_%d" % j
            prob += lpSum(asig_est[(i,j)] for i in self.ESTUDIANTES) <= self.CUPOS[j], labelB

        # Restriccion D: Si el estudiante fue asignado a una seccion, esta debe ser de uno de los cursos que el desea tomar
        for i in self.ESTUDIANTES:
           label = "EstAsig_%d" % i
           prob += lpSum(asig_est[(i,j)] for j in self.SECCIONES if self.EST_X_CUR[i][self.SEC_X_CUR[j]] == 0 ) == 0, label

        # Restriccion E: Un estudiante no puede tomar dos o más cursos que se dictan el mismo día
        for i in self.ESTUDIANTES:
           for h in self.HORARIOS:
               prob += lpSum(asig_est[(i, j)] for j in self.SECCIONES if self.SEC_X_HOR[j] == h) <= 1

        # Solucionar el problema a través de PuLP
        prob.writeLP("MinmaxProblem.lp")
        prob.solve()

        print("Status:", LpStatus[prob.status])
        print("Est, Curso, Secc = Asig, deseo")
        for i in self.ESTUDIANTES:
            for j in self.SECCIONES:
                if asig_est[(i,j)].varValue > 0:
                    print(i, "  ,", self.SEC_X_CUR[j],"  ", j, " =    ", asig_est[(i, j)].varValue, self.EST_X_CUR[i][self.SEC_X_CUR[j]])


    def calcularPrioridad(v_creditosPrerequisito, v_creditosTomados):
        #entre más creditosTomados, mayor prioridad
        #si los creditosPrerequisito es igual o mayor a creditosTomados, entonces se le brinda mayor prioridad
        #es más importante la antiguedad del estudiante (creditosTomados) que los prerequisitos.

        # Precondiciones: los prerequisitos y tomados siempren deben ser iguales o superiores a cero.
        if v_creditosTomados < 0:
            v_creditosTomados = 0
        if v_creditosPrerequisito < 0:
            v_creditosPrerequisito = 0

        l_prioridad = 1
        if (v_creditosPrerequisito <= v_creditosTomados):
            l_prioridad = 1 + (v_creditosTomados - v_creditosPrerequisito)

        l_prioridad = l_prioridad + 2*v_creditosTomados

        return l_prioridad

# FIN ASIGNACION_OPTIMA
solver = AsignadorCupos()
solver.poblar_estudiantesBD()
solver.asignacion_optima()