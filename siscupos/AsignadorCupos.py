#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Optimizador de asignacion de CUPOS
Authors: Grupo MisoAgiles 2014
"""

from pulp import *
import psycopg2

class Seccion:
    #########################################################################################
    # declaración de variables de la clase
    #
    horario = 'L'
    cupos = 0
    id_asignatura = 0
    id_seccion = 0
    def __init__(self):
        print("Creacion seccion")

class AsignadorCupos:
    #########################################################################################
    # declaración de variables de la clase
    #
    ESTUDIANTES = {} # dado el id del estudiante, encontrar la posición en el arreglo
    CURSOS = {}      # dado el id de la asignatura, encontrar la posicion en el arreglo
    SECCIONES = []   # la posición i almacena la sección
    HORARIOS = ['L', 'M', 'C', 'J', 'V', 'S'] # representan los días de la semana

    # EST_X_CUR[i][j] = 1, Si el estudiante i desea tomar el curso j
    #                 = 0, si el estudiante i no desea tomar el curso j
    EST_X_CUR = [[0 for i in range(1000)] for i in range(1000)]

    def __init__(self):
        print("Creacion")
        self.ESTUDIANTES = {}
        self.CURSOS = {}
        self.SECCIONES = []
        self.HORARIOS = ['L', 'M', 'C', 'J', 'V', 'S']
        self.EST_X_CUR = [[0 for i in range(1000)] for i in range(1000)]




    #################################################################################
    #
    # Poblar el arreglo de ESTUDIANTES y los cursos que desean tomar en los próximos
    # semestres
    #
    def poblar_estudiantesBD(self, periodoOptimizacion):

        #Obtiene la conexion
        try:
          conn = psycopg2.connect("dbname='d8iv5ac7d1jos6' user='kpbaqcwlfpqkgw' host='ec2-23-23-183-5.compute-1.amazonaws.com' password='4KLEgGfQDTQN2qgVYUo6DJfXiy'")
        except Exception:
          print "Fallo la conexion a la base de datos"

        #Crea los cursores para la ejecucion de las consultas
        curEstudiantes = conn.cursor()
        curCursos = conn.cursor()
        curSecciones = conn.cursor()
        curEstudiCur = conn.cursor()

        try:
            indice = 0
            curEstudiantes.execute("SELECT id from siscupos_estudiante order by id")
            rowsEstudiantes = curEstudiantes.fetchall()
            for rowE in rowsEstudiantes:
               # se mapea el id del estudiante con la posición en el arreglo.
               self.ESTUDIANTES[rowE[0]] = indice
               indice = indice + 1

            indice = 0
            curCursos.execute("SELECT id from siscupos_asignatura order by id")
            rowsCursos = curCursos.fetchall()
            for rowC in rowsCursos:
               # se mapea el id de la asignatura con la posición en el arreglo.
               self.CURSOS[rowC[0]] = indice
               indice = indice + 1


            #El siguiente query aplica pues solo se tiene un programa academico, en la siguiente version del optimizador
            #se deben tener en cuenta los programas => se debe modificar el query
            print "Consulta de preprogramacion"
            curSecciones.execute(' select                        '
                                 '       prp.id                  '
                                 '      ,axp.asignatura_id       '
                                 '      ,prp.cupos cupos         '
                                 '      ,prp."diaSemana"           '
                                 ' from siscupos_asignaturaxprograma axp '
                                 '    , siscupos_preprogramacion prp '
                                 ' where prp."asignaturaXPrograma_id" = axp.id '
                                 ' order by prp.id '
            )

            rowsSecciones = curSecciones.fetchall()
            for rowP in rowsSecciones:
                seccion = Seccion()
                seccion.id_seccion = rowP[0]
                seccion.id_asignatura = rowP[1]
                seccion.cupos = rowP[2]
                seccion.horario = rowP[3]
                self.SECCIONES.append(seccion)


            print "ejecucion de deseos"
            curEstudiCur.execute(
                             " select axe.asignatura_id curso "
                             "     , axe.estudiante_id estudiante "
                             "     , a.credito_prerrequisitos creditos_prerequisitos "
                             "     , axe.periodo periodo2"
                             "     , ( "
                             "        select COALESCE(sum(COALESCE(a1.creditos,0)), 0) "
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

            #inicializar
            EST_X_CUR = [[0 for i in range(len(self.ESTUDIANTES)+1)] for j in range(len(self.CURSOS)+1)]

            rowsEstudiCur = curEstudiCur.fetchall()
            #inicializa los valores en 0
            for x in range(len(self.ESTUDIANTES)):
               for y in range(len(self.CURSOS)):
                  self.EST_X_CUR[x][y] = 0

            print "antes de asignar deseos"
            #actualiza los cursos deseados
            for rowEC in rowsEstudiCur:
               self.EST_X_CUR[self.ESTUDIANTES[rowEC[1]]][self.CURSOS[rowEC[0]]] = self.calcularPrioridad(rowEC[2], rowEC[4], rowEC[3] == periodoOptimizacion)

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
                                    [(i,j) for i in range(len(self.ESTUDIANTES))
                                              for j in range(len(self.SECCIONES))], 0, 1, LpBinary)

        #Inicialir asig_est
        for i in range(len(self.ESTUDIANTES)):
            for j in range(len(self.SECCIONES)):
              asig_est[(i,j)].varValue = 0

        ######################################################################################
        # Funcion objetivo: Maximizar el total de cupos asignados.
        #
        prob += lpSum(asig_est[(i,j)]*self.EST_X_CUR[i][self.CURSOS[self.SECCIONES[j].id_asignatura]] for i in range(len(self.ESTUDIANTES)) for j in range(len(self.SECCIONES))), "TotalAsignaciones"

        ######################################################################################
        # Restricciones del modelo de optimización
        #

        # Restriccion A: Un estudiante tiene un maximo de 2 cursos
        for i in range(len(self.ESTUDIANTES)):
            labelA = "maxCur_%d" % i
            prob += lpSum(asig_est[(i,j)] for j in range(len(self.SECCIONES))) <= 2, labelA

        # Restriccion B: Un estudiante no puede ser asignado a dos o más secciones del mismo curso
        for i in range(len(self.ESTUDIANTES)):
            for j in range(len(self.SECCIONES)):
                 prob += (lpSum(asig_est[(i, m)] for m in range(len(self.SECCIONES)) if m != j and self.SECCIONES[m].id_asignatura == self.SECCIONES[j].id_asignatura ) +
                          lpSum(asig_est[(i, j)] for m in range(len(self.SECCIONES)) if m == j ) <= 1)

        # Restriccion C: La asignacion a una sección no puede superar su cupo maximo
        for j in range(len(self.SECCIONES)):
            labelB = "maxCupos_%d" % j
            prob += lpSum(asig_est[(i,j)] for i in range(len(self.ESTUDIANTES))) <= self.SECCIONES[j].cupos, labelB

        # Restriccion D: Si el estudiante fue asignado a una seccion, esta debe ser de uno de los cursos que el desea tomar
        for i in range(len(self.ESTUDIANTES)):
           label = "EstAsig_%d" % i
           prob += lpSum(asig_est[(i,j)] for j in range(len(self.SECCIONES)) if self.EST_X_CUR[i][self.CURSOS[self.SECCIONES[j].id_asignatura]]==0)==0, label

        # Restriccion E: Un estudiante no puede tomar dos o más cursos que se dictan el mismo día
        for i in range(len(self.ESTUDIANTES)):
           for h in self.HORARIOS:
               prob += lpSum(asig_est[(i, j)] for j in range(len(self.SECCIONES)) if self.SECCIONES[j].horario == h) <= 1

        # Solucionar el problema a través de PuLP
        prob.writeLP("MinmaxProblem.lp")
        prob.solve()
        return asig_est


    ##############################################################################
    # Calcula la prioridad dada a un curso deseado, teniendo en cuenta
    # los creditosPrerquisito exigidos para esa asigatura y
    # los creditosTotales que ha cursado el estudiante
    #
    def calcularPrioridad(self, v_creditosPrerequisito, v_creditosTomados, esPeriodoOptimizar):
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
            l_prioridad = 4

        l_prioridad = l_prioridad + v_creditosTomados

        # se brinda mayor prioridad si la asignatura fue pedida para el proximo semestre por el estudiante
        if (esPeriodoOptimizar) :
            l_prioridad = l_prioridad + 2

        return l_prioridad


    from django.db import connection
    def persistirResultado(self, asig_est, periodoOptimizacion):

        #Obtiene la conexion
        try:
          conn = psycopg2.connect("dbname='d8iv5ac7d1jos6' user='kpbaqcwlfpqkgw' host='ec2-23-23-183-5.compute-1.amazonaws.com' password='4KLEgGfQDTQN2qgVYUo6DJfXiy'")
        except Exception:
          print "Fallo la conexion a la base de datos"

        #Cursores para realizar inserts
        curPerAsignacion = conn.cursor()
        curIdPreAsid = conn.cursor()
        curUpdPerAsignacion = conn.cursor()

        curPerAsignacion.execute("insert into siscupos_preasignacioncurso "
                                 " (codigo, "
                                 "  \"fechaCorrida\", "
                                 "  observacion,  "
                                 "  periodo) values "
                                 "    (2, CURRENT_DATE, 'OK', " + str(periodoOptimizacion) + ")")

        curUpdPerAsignacion.execute("update siscupos_preasignacioncurso "
                                    " set codigo = id ")
        conn.commit()

        curIdPreAsid.execute(" select max(id) from siscupos_preasignacioncurso ")
        rowsIdPreAsid = curIdPreAsid.fetchall()

        for rowID in rowsIdPreAsid:
           idPreAsig = rowID[0]

        for i in self.ESTUDIANTES.keys():
           for j in range(len(self.SECCIONES)):
             if asig_est[(self.ESTUDIANTES[i], j)].varValue > 0:
                curAsignaturaSugerida = conn.cursor()
                curAsignaturaSugerida.execute(
                    " insert into siscupos_asignaturasugerida ("
                    "  anno, estado, \"preAsignacionCurso_id\", "
                    "  estudiante_id,\"preProgramacion_id\") "
                    "  values (2014, 'OK', " +
                               str(idPreAsig)+ ", "+
                               str(i)+", "+
                               str(self.SECCIONES[j].id_seccion)+" ) ")


        conn.commit()


# FIN ASIGNACION_OPTIMA
#solver = AsignadorCupos()
#solver.poblar_estudiantesBD()
#solver.asignacion_optima()