# -*- coding: utf-8 -*-
TRUNCATE "siscupos_programaacademico","siscupos_asignatura","siscupos_asignaturaxprograma","siscupos_estudiante","siscupos_asignaturaxestudiante" CASCADE;
--ProgramaAcademico
insert into "siscupos_programaacademico" values (9001, 'MISO', 'Maestria en Ingenieria de Software', ' Ruby ');

--Asignatura
insert into "siscupos_asignatura" values (9001, 'MISO-4101', 'Procesos de desarrollo ágiles', 4	);
insert into "siscupos_asignatura" values (9002, 'MBIT-4201', 'Emprendimiento y Negocios Electrónicos', 4);
insert into "siscupos_asignatura" values (9003, 'MISIS-4426','Desarrollo de soluciones cloud', 4);
insert into "siscupos_asignatura" values (9004, 'MISO-4202', 'Mejoramiento de la productividad:Automatización', 4);
insert into "siscupos_asignatura" values (9005, 'MISO-4203', 'Gestión de proyectos de desarrollo de software', 4);
insert into "siscupos_asignatura" values (9006, 'MISO-4204', 'Fabricas de software', 4);
insert into "siscupos_asignatura" values (9007, 'MISO-4205', 'Mejoramiento de la experiencia del usuario', 4);
insert into "siscupos_asignatura" values (9008, 'MISO-4301', 'Proyecto integrador', 4);

--AsignaturaXPrograma
insert into "siscupos_asignaturaxprograma" values (9001, 'SI',  1, 0, 9001, 9001);
insert into "siscupos_asignaturaxprograma" values (9002, 'SI',  1, 0, 9002, 9001);
insert into "siscupos_asignaturaxprograma" values (9003, 'SI',  2, 8, 9003, 9001);
insert into "siscupos_asignaturaxprograma" values (9004, 'SI',  2, 8, 9004, 9001);
insert into "siscupos_asignaturaxprograma" values (9005, 'SI',  3, 12, 9005, 9001);
insert into "siscupos_asignaturaxprograma" values (9006, 'SI',  3, 12, 9006, 9001);
insert into "siscupos_asignaturaxprograma" values (9007, 'SI',  4, 20, 9007, 9001);
insert into "siscupos_asignaturaxprograma" values (9008, 'SI',  4, 20, 9008, 9001);


--Estudiante
insert into "siscupos_estudiante" values(9001, 2001, 'Cristo', 'Rodriguez');
insert into "siscupos_estudiante" values(9002, 2002, 'Fredy', 'Viera');
insert into "siscupos_estudiante" values(9003, 2003, 'Jhon', 'Rodriguez');
insert into "siscupos_estudiante" values(9004, 2004, 'Diego', 'Agudelo');
insert into "siscupos_estudiante" values(9005, 2005, 'Fredy', 'Sandoval');

--AsignaturaXEstudiante
--Esta tabla se debe llenar dependiendo del escenario que se quier probar
--La siguiente es la base
--insert into "siscupos_asignaturaxestudiante" values("id serial","cursada","estado","fechaAdicion","fechaRemocion","asignatura_id","estudiante_id")

COMMIT;

