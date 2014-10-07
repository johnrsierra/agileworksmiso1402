#Optimizador de asignacion de CUPOS
#Authors: Grupo MisoAgiles 2014 - modifcado

#import de la libreria de conexion a la BD
import psycopg2

# Import PuLP modeler functions
from pulp import *

from django.db import connection


def optimizarAutomatico():

    totalestudiantes = 0
    totalmaterias = 0
    ESTUDIANTES = []
    CURSOS = []
    #En mi opinion no se usa el arreglo de secciones
    SECCIONES = []
    #el numero de seccion debe ser unico, por tratarse de un diccionario, por lo tanto
    #la manera de almacenar es seccion como llave y curso como valor
    SEC_X_CUR = {}
    #Los cupos se almacenan por seccion, la llave del diccionario es la seccion y el valor el cupo
    CUPOS = {}

    #Obtiene la conexion
    #try:

        #conn = psycopg2.connect("dbname='d8iv5ac7d1jos6' user='kpbaqcwlfpqkgw' host='ec2-23-23-183-5.compute-1.amazonaws.com' password='4KLEgGfQDTQN2qgVYUo6DJfXiy'")
    #except Exception:
    #   print "Fallo la conexion a la base de datos"


    #Crea los cursores para la ejecucion de las consultas
    curEstudiantes = connection.cursor()
    curCursos = connection.cursor()
    curSecciones = connection.cursor()
    curEstudiCur = connection.cursor()

    try:
        curEstudiantes.execute("SELECT id from siscupos_estudiante")
        curCursos.execute("SELECT id from siscupos_asignatura")
        #El siguiente query aplica pues solo se tiene un programa academico, en la siguiente version del optimizador
        #se deben tener en cuenta los programas => se debe modificar el query
        curSecciones.execute('SELECT axp.asignatura_id curso, prp.seccion seccion, prp.cupos cupos from siscupos_asignaturaxprograma axp, siscupos_preprogramacion prp where prp."asignaturaXPrograma_id" = axp.id')
        curEstudiCur.execute("select asignatura_id curso, estudiante_id estudiante from siscupos_asignaturaxestudiante where cursada = 'N'")
    except Exception:
        print "Error ejecutando el query"

    #Obtiene el resultado para los estudiantes
    rowsEstudiantes = curEstudiantes.fetchall()
    rowsCursos = curCursos.fetchall()
    rowsSecciones = curSecciones.fetchall()
    rowsEstudiCur = curEstudiCur.fetchall()

    #recorre los resultados y los ingresa en la variable respectiva
    for rowE in rowsEstudiantes:
        ESTUDIANTES.append(rowE[0] - 9000)
        totalestudiantes= totalestudiantes + 1

    for rowC in rowsCursos:
        CURSOS.append(rowC[0] - 9000)
        totalmaterias = totalmaterias + 1

    for rowP in rowsSecciones:
        SEC_X_CUR[rowP[1]] = rowP[0] - 9000
        CUPOS[rowP[1]] = rowP[2]
        SECCIONES.append(rowP[1])

    #Estudiante Curso
    EST_X_CUR = [[0 for i in range(totalmaterias+1)] for i in range(totalestudiantes+1)]

    #inicializa los valores en 0
    for x in range (1, totalestudiantes+1):
        for y in range (1, totalmaterias+1):
            EST_X_CUR[x][y] = 0

    #actualiza los cursos deseados
    for rowEC in rowsEstudiCur:
        EST_X_CUR[rowEC[1]-9000][rowEC[0]-9000] = 1

    asig_est = optimizadorCursos(ESTUDIANTES, CURSOS, SECCIONES, SEC_X_CUR, CUPOS, EST_X_CUR)

    #Cursores para realizar inserts
    curPerAsignacion = conn.cursor()
    curIdPreAsid = conn.cursor()
    curUpdPerAsignacion = conn.cursor()

    curPerAsignacion.execute("insert into siscupos_preasignacioncurso (codigo, \"fechaCorrida\", observacion, periodo) values (2, CURRENT_DATE, 'OK', 20141)")
    curUpdPerAsignacion.execute("update siscupos_preasignacioncurso set codigo = id ")
    conn.commit()
    curIdPreAsid.execute(" select max(id) from siscupos_preasignacioncurso ")

    rowsIdPreAsid = curIdPreAsid.fetchall()
    for rowID in rowsIdPreAsid:
        idPreAsig = rowID[0]

    for i in ESTUDIANTES:
        for j in SECCIONES:
            if asig_est[(i, j)].varValue > 0:
                curAsignaturaSugerida = conn.cursor()
                curAsignaturaSugerida.execute(" insert into siscupos_asignaturasugerida (anno, estado, \"preAsignacionCurso_id\", estudiante_id,\"preProgramacion_id\") "
                                  "values (2014, 'OK', "+str(idPreAsig)+", "+str(i+9000)+", "+str(SEC_X_CUR[j])+" ) ")


    conn.commit()

    print 'LISTO'

def optimizadorCursos(v_estudiantes, v_cursos, v_secciones, v_sec_x_cur, v_cupos, v_est_x_cur):

    prob = LpProblem("AsignacionCursos", LpMaximize)

    asig_est = LpVariable.dicts("AsigSugerida",
                                [(i, j) for i in v_estudiantes
                                          for j in v_secciones], 0, 1, LpBinary)

    # Llenar los datos de prueba

    #for i in v_estudiantes:
    #    for j in v_secciones:
    #      asig_est[(i, j)].varValue = 0


    # Funcion objetivo
    prob += lpSum(asig_est[(i, j)] for i in v_estudiantes for j in v_secciones)


    # Restriccion D: Un estudiante es asignado a uno de los cursos que el desea asistir
    for i in v_estudiantes:
        prob += lpSum(v_est_x_cur[i][v_sec_x_cur[j]] for j in v_secciones if asig_est[(i, j)].varValue > 0) >= 1

    #== lpSum(1 for j in v_secciones if asig_est[(i, j)].varValue > 0)

    # Restriccion A: Un estudiante tiene un maximo de 2 cursos
    for i in v_estudiantes:
        prob += lpSum(asig_est[(i, j)] for j in v_secciones) <= 2

    # Restriccion B: Un estudiante no puede ser asignado a dos secciones del mismo curso
    #for k in v_cursos:
    #    for i in v_estudiantes:
    #        for j in v_secciones:
    #           prob += lpSum(asig_est[(i, j)].varValue * cur_x_sec[(k, j)].varValue for j in v_secciones) <= 1

    for j in v_secciones:
        prob += lpSum(asig_est[(i, j)] for i in v_estudiantes) <= v_cupos[j]

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    #print("Status:", LpStatus[prob.status])

    return asig_est