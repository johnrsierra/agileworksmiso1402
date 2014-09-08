# -*- coding: utf-8 -*-
--ProgramaAcademico
insert into "siscupos_programaacademico" values (1, 'MISO', 'Maestria en Ingenieria de Software', ' Ruby ');

--Asignatura
insert into "siscupos_asignatura" values (1, MISO-4101, Procesos de desarrollo ágiles, 4	);
insert into "siscupos_asignatura" values (2, MBIT-4201, Emprendimiento y Negocios Electrónicos, 4);
insert into "siscupos_asignatura" values (3, MISIS-4426, Desarrollo de soluciones cloud, 4);
insert into "siscupos_asignatura" values (4, MISO-4202, Mejoramiento de la productividad:Automatización, 4);
insert into "siscupos_asignatura" values (5, MISO-4203, Gestión de proyectos de desarrollo de software, 4);
insert into "siscupos_asignatura" values (6, MISO-4204, Fabricas de software, 4);
insert into "siscupos_asignatura" values (7, MISO-4205, Mejoramiento de la experiencia del usuario, 4);
insert into "siscupos_asignatura" values (8, MISO-4301, Proyecto integrador, 4);

--AsignaturaXPrograma
insert into "siscupos_asignaturaxprograma" values (1, 'SI',  1, 0, 1, 1);
insert into "siscupos_asignaturaxprograma" values (2, 'SI',  1, 0, 2, 1); 
insert into "siscupos_asignaturaxprograma" values (3, 'SI',  2, 8, 3, 1);
insert into "siscupos_asignaturaxprograma" values (4, 'SI',  2, 8, 4, 1);
insert into "siscupos_asignaturaxprograma" values (5, 'SI',  3, 12, 5, 1);
insert into "siscupos_asignaturaxprograma" values (6, 'SI',  3, 12, 6, 1);
insert into "siscupos_asignaturaxprograma" values (7, 'SI',  4, 20, 7, 1); 
insert into "siscupos_asignaturaxprograma" values (8, 'SI',  4, 20, 8, 1);


--Estudiante
insert into "siscupos_estudiante" values(1, 2001, "Cristo", "Rodriguez" )
insert into "siscupos_estudiante" values(2, 2002, "Fredy", "Viera")
insert into "siscupos_estudiante" values(3, 2003, "Jhon", "Rodriguez")
insert into "siscupos_estudiante" values(4, 2004, "Diego", "Agudelo")
insert into "siscupos_estudiante" values(5, 2005, "Fredy", "Sandoval")

--AsignaturaXEstudiante
--Esta tabla se debe llenar dependiendo del escenario que se quier probar
--La siguiente es la base
insert into "siscupos_asignaturaxestudiante" values("id serial","cursada","estado","fechaAdicion","fechaRemocion","asignatura_id","estudiante_id")



