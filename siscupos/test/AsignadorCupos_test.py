#!/usr/bin/env python
#-*- coding: utf-8 -*-
import siscupos.AsignadorCupos

import unittest


class AsignadorCupos(unittest.TestCase):

    def test_cupos_infinitos(self):
        solver = siscupos.AsignadorCupos.AsignadorCupos()
        solver.ESTUDIANTES[123] = 0
        solver.ESTUDIANTES[125] = 1
        solver.ESTUDIANTES[127] = 2
        solver.ESTUDIANTES[129] = 3
        solver.ESTUDIANTES[131] = 4
        solver.ESTUDIANTES[133] = 5
        solver.ESTUDIANTES[135] = 6
        solver.ESTUDIANTES[139] = 7
        solver.ESTUDIANTES[141] = 8
        solver.ESTUDIANTES[143] = 9

        solver.CURSOS[10] = 0
        solver.CURSOS[20] = 1
        solver.CURSOS[30] = 2
        solver.CURSOS[40] = 3

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 100
        seccion.id_asignatura = 10
        seccion.cupos = 1000
        seccion.horario = 'L'
        solver.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 100
        seccion.id_asignatura = 10
        seccion.cupos = 1000
        seccion.horario = 'L'
        solver.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 200
        seccion.id_asignatura = 20
        seccion.cupos = 1001
        seccion.horario = 'M'
        solver.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 300
        seccion.id_asignatura = 30
        seccion.cupos = 1002
        seccion.horario = 'C'
        solver.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 400
        seccion.id_asignatura = 40
        seccion.cupos = 1003
        seccion.horario = 'J'
        solver.SECCIONES.append(seccion)

        solver.EST_X_CUR = [[0 for i in range(len(solver.CURSOS)+1)] for j in range(len(solver.ESTUDIANTES)+1)]
        solver.EST_X_CUR[0][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[0][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[1][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[1][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[2][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[2][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[3][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[3][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[4][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[4][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[5][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[5][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[6][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[6][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[7][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[7][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[8][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[8][1] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[9][0] = solver.calcularPrioridad(0, 4)
        solver.EST_X_CUR[9][1] = solver.calcularPrioridad(0, 4)



        asig_est = solver.asignacion_optima()

        self.aux_soloSeAsignanDeseados(solver.ESTUDIANTES, solver.SECCIONES, solver.CURSOS, solver.EST_X_CUR, asig_est)
        self.aux_limiteCupos(solver.ESTUDIANTES, solver.SECCIONES, solver.CURSOS, solver.EST_X_CUR, asig_est)



    def test_cupos_limitados(self):
        print("Test cupos limitados")
        s = siscupos.AsignadorCupos.AsignadorCupos()
        s.ESTUDIANTES[123] = 0
        s.ESTUDIANTES[125] = 1
        s.ESTUDIANTES[127] = 2
        s.ESTUDIANTES[129] = 3
        s.ESTUDIANTES[131] = 4
        s.ESTUDIANTES[133] = 5
        s.ESTUDIANTES[135] = 6
        s.ESTUDIANTES[139] = 7
        s.ESTUDIANTES[141] = 8
        s.ESTUDIANTES[143] = 9

        s.CURSOS[10] = 0
        s.CURSOS[20] = 1
        s.CURSOS[30] = 2
        s.CURSOS[40] = 3

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 100
        seccion.id_asignatura = 10
        seccion.cupos = 1
        seccion.horario = 'L'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 100
        seccion.id_asignatura = 10
        seccion.cupos = 2
        seccion.horario = 'L'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 200
        seccion.id_asignatura = 20
        seccion.cupos = 3
        seccion.horario = 'M'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 300
        seccion.id_asignatura = 30
        seccion.cupos = 4
        seccion.horario = 'C'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 400
        seccion.id_asignatura = 40
        seccion.cupos = 5
        seccion.horario = 'J'
        s.SECCIONES.append(seccion)

        s.EST_X_CUR = [[0 for i in range(len(s.CURSOS)+1)] for j in range(len(s.ESTUDIANTES)+1)]
        s.EST_X_CUR[0][0] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[0][1] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[1][0] = s.calcularPrioridad(0, 32)
        s.EST_X_CUR[1][1] = s.calcularPrioridad(0, 32)
        s.EST_X_CUR[2][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[2][1] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[3][0] = s.calcularPrioridad(0, 40)
        s.EST_X_CUR[3][1] = s.calcularPrioridad(0, 40)
        s.EST_X_CUR[4][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[4][1] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[5][0] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[5][1] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[6][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[6][1] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[7][0] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[7][1] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[8][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[8][1] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[9][0] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[9][1] = s.calcularPrioridad(0, 16)



        asig_est = s.asignacion_optima()


        print("Est, Curso, Secc = Asig, deseo")
        for i in range(len(s.ESTUDIANTES)):
            for j in range(len(s.SECCIONES)):
                if asig_est[(i,j)].varValue > 0:
                    print(i, s.SECCIONES[j].id_asignatura, j, '=',  asig_est[(i, j)].varValue, s.EST_X_CUR[i][s.CURSOS[s.SECCIONES[j].id_asignatura]])

        self.aux_soloSeAsignanDeseados(s.ESTUDIANTES, s.SECCIONES, s.CURSOS, s.EST_X_CUR, asig_est)
        self.aux_limiteCupos(s.ESTUDIANTES, s.SECCIONES, s.CURSOS, s.EST_X_CUR, asig_est)



    def aux_soloSeAsignanDeseados(self, ESTUDIANTES, SECCIONES, CURSOS, EST_X_CUR, asig_est):
        for i in range(len(ESTUDIANTES)):
            for j in range(len(SECCIONES)):
                self.assertGreaterEqual(EST_X_CUR[i][CURSOS[SECCIONES[j].id_asignatura]], asig_est[(i,j)].varValue, "No se puede asignar un curso que no se desea tomar")


    def aux_limiteCupos(self, ESTUDIANTES, SECCIONES, CURSOS, EST_X_CUR, asig_est):
        for j in range(len(SECCIONES)):
            cuposUsados = 0
            for i in range(len(ESTUDIANTES)):
                cuposUsados = cuposUsados + asig_est[(i,j)].varValue

            print(j, 'Cupos usados=', cuposUsados, 'Cupos seccion=', SECCIONES[j].cupos)
            self.assertGreaterEqual(SECCIONES[j].cupos, cuposUsados, "No se debe sobrepasar el CUPO")




    #Si solo hay un cupo, este debe ser asignado al estudiante mas viejo
    #Este estudiante sera el id 133
    def test_prioridad_ultimo_semestre(self):
        print("Test cupos limitados")
        s = siscupos.AsignadorCupos.AsignadorCupos()
        s.ESTUDIANTES[123] = 0
        s.ESTUDIANTES[125] = 1
        s.ESTUDIANTES[127] = 2
        s.ESTUDIANTES[129] = 3
        s.ESTUDIANTES[131] = 4
        s.ESTUDIANTES[133] = 5
        s.ESTUDIANTES[135] = 6
        s.ESTUDIANTES[139] = 7
        s.ESTUDIANTES[141] = 8
        s.ESTUDIANTES[143] = 9

        s.CURSOS[10] = 0
        s.CURSOS[20] = 1
        s.CURSOS[30] = 2
        s.CURSOS[40] = 3

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 100
        seccion.id_asignatura = 10
        seccion.cupos = 1
        seccion.horario = 'L'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 200
        seccion.id_asignatura = 20
        seccion.cupos = 1
        seccion.horario = 'C'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 300
        seccion.id_asignatura = 30
        seccion.cupos = 1
        seccion.horario = 'J'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 400
        seccion.id_asignatura = 40
        seccion.cupos = 1
        seccion.horario = 'V'
        s.SECCIONES.append(seccion)

        s.EST_X_CUR = [[0 for i in range(len(s.CURSOS)+1)] for j in range(len(s.ESTUDIANTES)+1)]
        s.EST_X_CUR[0][0] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[0][1] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[1][0] = s.calcularPrioridad(0, 32)
        s.EST_X_CUR[1][1] = s.calcularPrioridad(0, 32)
        s.EST_X_CUR[2][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[2][1] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[3][0] = s.calcularPrioridad(0, 36)
        s.EST_X_CUR[3][1] = s.calcularPrioridad(0, 36)
        s.EST_X_CUR[4][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[4][1] = s.calcularPrioridad(0, 4)

        # El estudiante id 133, tiene acumulados 40 creditos
        s.EST_X_CUR[5][0] = s.calcularPrioridad(0, 40) # curso 10
        s.EST_X_CUR[5][1] = s.calcularPrioridad(0, 40) # curso 20

        s.EST_X_CUR[6][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[6][1] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[7][0] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[7][1] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[8][0] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[8][1] = s.calcularPrioridad(0, 4)
        s.EST_X_CUR[9][0] = s.calcularPrioridad(0, 16)
        s.EST_X_CUR[9][1] = s.calcularPrioridad(0, 16)



        asig_est = s.asignacion_optima()

        self.aux_soloSeAsignanDeseados(s.ESTUDIANTES, s.SECCIONES, s.CURSOS, s.EST_X_CUR, asig_est)
        self.aux_limiteCupos(s.ESTUDIANTES, s.SECCIONES, s.CURSOS, s.EST_X_CUR, asig_est)

        #el estudiante con indice '5' es el màs viejo (40 creditos) por lo cual se respeta su deseo
        for j in range(len(s.SECCIONES)):
            if s.SECCIONES[j].id_asignatura == 20 or s.SECCIONES[j].id_asignatura == 10:
                self.assertEquals(asig_est[(5,j)].varValue, 1, 'El estudiante mas viejo no obtuvo cupo')


#        print("Est, Curso, Secc = Asig, deseo")
#        for i in range(len(s.ESTUDIANTES)):
#            for j in range(len(s.SECCIONES)):
#                if asig_est[(i,j)].varValue > 0:
#                    print(i,   s.SECCIONES[j].id_asignatura,       j, '=',  asig_est[(i, j)].varValue, s.EST_X_CUR[i][s.CURSOS[s.SECCIONES[j].id_asignatura]])


    #Si solo hay un cupo, este debe ser asignado al estudiante mas viejo
    #Este estudiante sera el id 133
    def test_prioridad_seleccion_prox_semestre(self):
        print("Test cupos limitados")
        s = siscupos.AsignadorCupos.AsignadorCupos()
        s.ESTUDIANTES[123] = 0
        s.ESTUDIANTES[125] = 1
        s.ESTUDIANTES[127] = 2
        s.ESTUDIANTES[129] = 3
        s.ESTUDIANTES[131] = 4
        s.ESTUDIANTES[133] = 5
        s.ESTUDIANTES[135] = 6
        s.ESTUDIANTES[139] = 7
        s.ESTUDIANTES[141] = 8
        s.ESTUDIANTES[143] = 9

        s.CURSOS[10] = 0
        s.CURSOS[20] = 1
        s.CURSOS[30] = 2
        s.CURSOS[40] = 3

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 100
        seccion.id_asignatura = 10
        seccion.cupos = 1
        seccion.horario = 'L'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 200
        seccion.id_asignatura = 20
        seccion.cupos = 1
        seccion.horario = 'C'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 300
        seccion.id_asignatura = 30
        seccion.cupos = 1
        seccion.horario = 'J'
        s.SECCIONES.append(seccion)

        seccion = siscupos.AsignadorCupos.Seccion()
        seccion.id_seccion = 400
        seccion.id_asignatura = 40
        seccion.cupos = 1
        seccion.horario = 'V'
        s.SECCIONES.append(seccion)

        s.EST_X_CUR = [[0 for i in range(len(s.CURSOS)+1)] for j in range(len(s.ESTUDIANTES)+1)]
        s.EST_X_CUR[0][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[0][1] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[1][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[1][1] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[2][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[2][1] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[3][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[3][1] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[4][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[4][1] = s.calcularPrioridad(0, 16, 0)

        # El estudiante id 133, desea ver las materias el proximo semestre
        s.EST_X_CUR[5][0] = s.calcularPrioridad(0, 16, 1) # curso 10
        s.EST_X_CUR[5][1] = s.calcularPrioridad(0, 16, 1) # curso 20

        s.EST_X_CUR[6][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[6][1] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[7][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[7][1] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[8][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[8][1] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[9][0] = s.calcularPrioridad(0, 16, 0)
        s.EST_X_CUR[9][1] = s.calcularPrioridad(0, 16, 0)



        asig_est = s.asignacion_optima()

        self.aux_soloSeAsignanDeseados(s.ESTUDIANTES, s.SECCIONES, s.CURSOS, s.EST_X_CUR, asig_est)
        self.aux_limiteCupos(s.ESTUDIANTES, s.SECCIONES, s.CURSOS, s.EST_X_CUR, asig_est)

        #el estudiante con indice '5' seleccion las materoas 20 y 10 para el proximo semestre
        for j in range(len(s.SECCIONES)):
            if s.SECCIONES[j].id_asignatura == 20 or s.SECCIONES[j].id_asignatura == 10:
                self.assertEquals(asig_est[(5,j)].varValue, 1, 'El estudiante mas viejo no obtuvo cupo')


#        print("Est, Curso, Secc = Asig, deseo")
#        for i in range(len(s.ESTUDIANTES)):
#            for j in range(len(s.SECCIONES)):
#                if asig_est[(i,j)].varValue > 0:
#                    print(i,   s.SECCIONES[j].id_asignatura,       j, '=',  asig_est[(i, j)].varValue, s.EST_X_CUR[i][s.CURSOS[s.SECCIONES[j].id_asignatura]])








    def aux_soloSeAsignanDeseados(self, ESTUDIANTES, SECCIONES, CURSOS, EST_X_CUR, asig_est):
        for i in range(len(ESTUDIANTES)):
            for j in range(len(SECCIONES)):
                self.assertGreaterEqual(EST_X_CUR[i][CURSOS[SECCIONES[j].id_asignatura]], asig_est[(i,j)].varValue, "No se puede asignar un curso que no se desea tomar")


    def aux_limiteCupos(self, ESTUDIANTES, SECCIONES, CURSOS, EST_X_CUR, asig_est):
        for j in range(len(SECCIONES)):
            cuposUsados = 0
            for i in range(len(ESTUDIANTES)):
                cuposUsados = cuposUsados + asig_est[(i,j)].varValue

            print(j, 'Cupos usados=', cuposUsados, 'Cupos seccion=', SECCIONES[j].cupos)
            self.assertGreaterEqual(SECCIONES[j].cupos, cuposUsados, "No se debe sobrepasar el CUPO")


if __name__ == '__main__':
    unittest.main()
