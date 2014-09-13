"""
Optimizador de asignacion de CUPOS

Authors: Grupo MisoAgiles 2014
"""

# Import PuLP modeler functions
from pulp import *


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
    