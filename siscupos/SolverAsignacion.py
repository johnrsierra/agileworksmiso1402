#Optimizador de asignacion de CUPOS
#Authors: Grupo MisoAgiles 2014

#import de la libreria de conexion a la BD
import psycopg2

# Import PuLP modeler functions
from pulp import *

#Informacion necesaria
totalestudiantes = 0
totalmaterias = 0
#COlecciones de dato
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


prob = LpProblem("AsignacionCursos", LpMaximize)

asig_est = LpVariable.dicts("AsigSugerida",
                            [(i, j) for i in ESTUDIANTES
                                      for j in SECCIONES], 0, 1, LpBinary)


#for i in ESTUDIANTES:
#    for j in SECCIONES:
#      asig_est[(i, j)].varValue = 0


# Funcion objetivo
prob += lpSum(asig_est[(i, j)] for i in ESTUDIANTES for j in SECCIONES)


# Restriccion D: Un estudiante es asignado a uno de los cursos que el desea asistir
for i in ESTUDIANTES:
    prob += lpSum(EST_X_CUR[i][SEC_X_CUR[j]] for j in SECCIONES if asig_est[(i, j)].varValue > 0) >= 1

#== lpSum(1 for j in SECCIONES if asig_est[(i, j)].varValue > 0)

# Restriccion A: Un estudiante tiene un maximo de 2 cursos
for i in ESTUDIANTES:
    prob += lpSum(asig_est[(i, j)] for j in SECCIONES) <= 2

# Restriccion B: Un estudiante no puede ser asignado a dos secciones del mismo curso
#for k in CURSOS:
#    for i in ESTUDIANTES:
#        for j in SECCIONES:
#           prob += lpSum(asig_est[(i, j)].varValue * cur_x_sec[(k, j)].varValue for j in SECCIONES) <= 1

# Restriccion C: La asignacion a una seccion no puede superar su cupo maximo
for j in SECCIONES:
    prob += lpSum(asig_est[(i, j)] for i in ESTUDIANTES) <= CUPOS[j]

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])


for i in ESTUDIANTES:
    print("Estudiante: ", i)
    print(lpSum( EST_X_CUR[i][SEC_X_CUR[j]] for j in SECCIONES if asig_est[(i, j)].varValue > 0), " = ", lpSum(1 for j in SECCIONES if asig_est[(i, j)].varValue > 0) )
    for j in SECCIONES:
        print("    est_x_cur: ", j,  EST_X_CUR[i][SEC_X_CUR[j]], "asignacion a la secc ", j, " = ", asig_est[(i, j)].varValue)


for i in ESTUDIANTES:
    for j in SECCIONES:
        if asig_est[(i, j)].varValue > 0:
            print(i, ",", SEC_X_CUR[j], " = ", asig_est[(i, j)].varValue, EST_X_CUR[i][SEC_X_CUR[j]])
