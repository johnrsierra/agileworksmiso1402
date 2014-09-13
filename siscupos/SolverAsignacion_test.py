import unittest
from pulp import *
from SolverAsignacion import *

class TestSolveAsignacion(unittest.TestCase):
    def setUp(self):
        # Arreglo de codigos de ESTUDIANTES
        self.vl_estudiantes = ['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12','E13','E14','E15','E16','E17','E18','E19','E20']
        # Arreglo de codigos de CURSOS
        self.vl_cursos = ['C1','C2','C3','C4']
        # Arreglo de codigos de SECCIONES
        self.vl_secciones = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']

        # Diccionario de SECCIONES por CURSOS
        self.vl_sec_x_cur = {
            'S1': 'C1',
            'S2': 'C1',
            'S3': 'C2',
            'S4': 'C3',
            'S5': 'C4',
            'S6': 'C4'
        }

        # Diccionario de CUPOS disponibles por SECCION
        self.vl_cupos = {
            'S1': 5,
            'S2': 5,
            'S3': 5,
            'S4': 5,
            'S5': 5,
            'S6': 5
        }

        # Matriz de cruce de ESTUDIANTES con CURSOS. Se utilizan arreglos a partir del numero cero
        # siguiendo el la secuencia: vl_est_x_cur[ESTUDIANTE 0..n][CURSO 0..n]
        self.vl_est_x_cur = [[0 for i in range(5)] for i in range(21)]
        self.vl_est_x_cur[0][0] = 1
        self.vl_est_x_cur[0][1] = 0
        self.vl_est_x_cur[0][2] = 1
        self.vl_est_x_cur[0][3] = 0
        self.vl_est_x_cur[1][0] = 0
        self.vl_est_x_cur[1][1] = 0
        self.vl_est_x_cur[1][2] = 0
        self.vl_est_x_cur[1][3] = 0
        self.vl_est_x_cur[2][0] = 0
        self.vl_est_x_cur[2][1] = 0
        self.vl_est_x_cur[2][2] = 1
        self.vl_est_x_cur[2][3] = 1
        self.vl_est_x_cur[3][0] = 1
        self.vl_est_x_cur[3][1] = 1
        self.vl_est_x_cur[3][2] = 0
        self.vl_est_x_cur[3][3] = 0
        self.vl_est_x_cur[4][0] = 0
        self.vl_est_x_cur[4][1] = 1
        self.vl_est_x_cur[4][2] = 1
        self.vl_est_x_cur[4][3] = 0
        self.vl_est_x_cur[5][0] = 0
        self.vl_est_x_cur[5][1] = 1
        self.vl_est_x_cur[5][2] = 0
        self.vl_est_x_cur[5][3] = 1
        self.vl_est_x_cur[6][0] = 1
        self.vl_est_x_cur[6][1] = 1
        self.vl_est_x_cur[6][2] = 0
        self.vl_est_x_cur[6][3] = 0
        self.vl_est_x_cur[7][0] = 0
        self.vl_est_x_cur[7][1] = 0
        self.vl_est_x_cur[7][2] = 1
        self.vl_est_x_cur[7][3] = 0
        self.vl_est_x_cur[8][0] = 0
        self.vl_est_x_cur[8][1] = 0
        self.vl_est_x_cur[8][2] = 0
        self.vl_est_x_cur[8][3] = 1
        self.vl_est_x_cur[9][0] = 1
        self.vl_est_x_cur[9][1] = 1
        self.vl_est_x_cur[9][2] = 0
        self.vl_est_x_cur[9][3] = 0
        self.vl_est_x_cur[10][0] = 1
        self.vl_est_x_cur[10][1] = 0
        self.vl_est_x_cur[10][2] = 1
        self.vl_est_x_cur[10][3] = 1
        self.vl_est_x_cur[11][0] = 1
        self.vl_est_x_cur[11][1] = 0
        self.vl_est_x_cur[11][2] = 0
        self.vl_est_x_cur[11][3] = 0
        self.vl_est_x_cur[12][0] = 1
        self.vl_est_x_cur[12][1] = 1
        self.vl_est_x_cur[12][2] = 0
        self.vl_est_x_cur[12][3] = 0
        self.vl_est_x_cur[13][0] = 1
        self.vl_est_x_cur[13][1] = 1
        self.vl_est_x_cur[13][2] = 1
        self.vl_est_x_cur[13][3] = 0
        self.vl_est_x_cur[14][0] = 0
        self.vl_est_x_cur[14][1] = 0
        self.vl_est_x_cur[14][2] = 0
        self.vl_est_x_cur[14][3] = 1
        self.vl_est_x_cur[15][0] = 0
        self.vl_est_x_cur[15][1] = 0
        self.vl_est_x_cur[15][2] = 0
        self.vl_est_x_cur[15][3] = 0
        self.vl_est_x_cur[16][0] = 0
        self.vl_est_x_cur[16][1] = 1
        self.vl_est_x_cur[16][2] = 1
        self.vl_est_x_cur[16][3] = 0
        self.vl_est_x_cur[17][0] = 0
        self.vl_est_x_cur[17][1] = 1
        self.vl_est_x_cur[17][2] = 0
        self.vl_est_x_cur[17][3] = 0
        self.vl_est_x_cur[18][0] = 1
        self.vl_est_x_cur[18][1] = 1
        self.vl_est_x_cur[18][2] = 0
        self.vl_est_x_cur[18][3] = 1
        self.vl_est_x_cur[19][0] = 1
        self.vl_est_x_cur[19][1] = 0
        self.vl_est_x_cur[19][2] = 1
        self.vl_est_x_cur[19][3] = 0
        
        self.vl_asig_est = optimizadorCursos(self.vl_estudiantes, self.vl_cursos, self.vl_secciones, self.vl_sec_x_cur, self.vl_cupos, self.vl_est_x_cur)

    def testEjecucionOptimizador(self):
        self.assertTrue(self.vl_asig_est)

    def testEstudiantesDeOptimizadorExisten(self):
        #Obtiene las llaves de los valores retornados del optimizados las cuales se compones
        # de un listado ('CODIGO ESTUDIANTES', 'CODIGO SECCION')
        for i_keys in self.vl_asig_est.keys():
            # Se obtiene el CODIGO ESTUDIANTE y se verifica que exista en el listado de ESTUDIANTES
            self.assertTrue( i_keys[0] in self.vl_estudiantes )
            
    def testSeccionesDeOptimizadorExisten(self):
        #Obtiene las llaves de los valores retornados del optimizados las cuales se compones
        # de un listado ('CODIGO ESTUDIANTES', 'CODIGO SECCION')
        for i_keys in self.vl_asig_est.keys():
            # Se obtiene el CODIGO SECCION y se verifica que exista en el listado de SECCIONES
            self.assertTrue( i_keys[1] in self.vl_secciones )
    
    def testEstudianteMaximoDosCursos(self):
        #Obtiene el par Indice y Valor del listado de ESTUDIANTES y se recorre dicho listado
        for i_idx, i_val in enumerate(self.vl_estudiantes):
            vl_cursosAsignadoEstudiante =[]
            #Obtiene el par Indice y Valor del listado de SECCIONES y se recorre dicho listado
            for j_idx, j_val in enumerate(self.vl_secciones):
                #Se evalua que exista la llave ('CODIGO ESTUDIANTES', 'CODIGO SECCION') en el listado
                # que retorno el optimizador y cuyo valor sea '1' lo cual indica asignaci?n
                if self.vl_asig_est[(i_val, j_val)].varValue > 0:
                    # Se agrega el valor del diccionario de CURSOS usando la llave de SECCIONES
                    #print(i_val, ",", j_val, ',', self.vl_sec_x_cur[j_val], " = ", self.vl_asig_est[(i_val, j_val)].varValue)#, asig_est[(i_val, j_val)].value())
                    vl_cursosAsignadoEstudiante.append(self.vl_sec_x_cur[j_val])
            #print i_val, vl_cursosEstudiante
            #print(i_val, ",", j_val, ',', self.vl_sec_x_cur[j_val], " = ", self.vl_asig_est[(i_val, j_val)].varValue)#, asig_est[(i_val, j_val)].value())
            #print len(list(set(vl_cursosEstudiante)))
            # Se verifica que el la longitud maxima de los cursos asignados sea menor o igual a 2
            self.assertLessEqual(len(list(set(vl_cursosAsignadoEstudiante))) , 2)
    

    def testEstudianteAsignadoAlmenosUnCursoDeseo(self):
        #Obtiene el par Indice y Valor del listado de ESTUDIANTES y se recorre dicho listado
        for i_idx, i_val in enumerate(self.vl_estudiantes):
            vl_totalAsignacionCursosDeseo = 0
            vl_cursosAsignadoEstudiante =[]
            #Obtiene el par Indice y Valor del listado de SECCIONES y se recorre dicho listado
            for j_idx, j_val in enumerate(self.vl_secciones):
                #Se evalua que exista la llave ('CODIGO ESTUDIANTES', 'CODIGO SECCION') en el listado
                # que retorno el optimizador y cuyo valor sea '1' lo cual indica asignaci?n
                if self.vl_asig_est[(i_val, j_val)].varValue > 0:
                    # Se agrega el valor del diccionario de CURSOS usando la llave de SECCIONES
                    vl_cursosAsignadoEstudiante.append(self.vl_sec_x_cur[j_val])
            
            
            #Obtiene el par Indice y Valor del listado de CURSOS y se recorre dicho listado
            for k_idx, k_val in enumerate(self.vl_cursos):
                #Se evalua que exista un cruce en la matriz ESTUDIANTES X CURSO  (valor a 1)
                if self.vl_est_x_cur[i_idx][k_idx] == 1 :
                    # A partir del valor del recorrido se evalua que el CURSO corresponda a los cursos que ha sido asignado
                    if k_val in vl_cursosAsignadoEstudiante :
                        vl_totalAsignacionCursosDeseo += 1
            
            # Se evalua que almenos se haya asignado a un curso de deseo
            #print i_val, k_val, vl_cursosAsignadoEstudiante, vl_totalAsignacionCursosDeseo
            self.assertGreaterEqual(vl_totalAsignacionCursosDeseo, 1)
            
    
    def _testEstudianteNoAsignadoCursoNoDeseo(self):
        #Obtiene el par Indice y Valor del listado de ESTUDIANTES y se recorre dicho listado
        for i_idx, i_val in enumerate(self.vl_estudiantes):
            vl_cursosAsignadoEstudiante =[]
            #Obtiene el par Indice y Valor del listado de SECCIONES y se recorre dicho listado
            for j_idx, j_val in enumerate(self.vl_secciones):
                #Se evalua que exista la llave ('CODIGO ESTUDIANTES', 'CODIGO SECCION') en el listado
                # que retorno el optimizador y cuyo valor sea '1' lo cual indica asignaci?n
                if self.vl_asig_est[(i_val, j_val)].varValue > 0:
                    vl_cursosAsignadoEstudiante.append(self.vl_sec_x_cur[j_val])
            
            #Obtiene el par Indice y Valor del listado de CURSOS y se recorre dicho listado
            for k_idx, k_val in enumerate(self.vl_cursos):
                #Se evalua que exista un cruce en la matriz ESTUDIANTES X CURSO  (valor a 1)
                if self.vl_est_x_cur[i_idx][k_idx] == 1 :
                    # Se evalua que el CURSO al cual ha sido asignado corresponde a un curso deseado
                    self.assertTrue( k_val in vl_cursosAsignadoEstudiante )
