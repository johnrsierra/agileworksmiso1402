BEGIN;
CREATE TABLE "siscupos_asignatura" (
    "id" integer NOT NULL PRIMARY KEY,
    "codigo" varchar(20) NOT NULL,
    "nombres" varchar(200) NOT NULL,
    "creditos" integer NOT NULL
)
;
CREATE TABLE "siscupos_programaacademico" (
    "id" integer NOT NULL PRIMARY KEY,
    "sigla" varchar(10) NOT NULL,
    "nombre" varchar(200) NOT NULL,
    "nombreCoordinador" varchar(200) NOT NULL
)
;
CREATE TABLE "siscupos_asignaturaxprograma" (
    "id" integer NOT NULL PRIMARY KEY,
    "esefectivo" varchar(2) NOT NULL,
    "semestresugerido" integer NOT NULL,
    "creditosPrerequisitos" integer NOT NULL,
    "asignatura_id" integer NOT NULL REFERENCES "siscupos_asignatura" ("id"),
    "programaAcademico_id" integer NOT NULL REFERENCES "siscupos_programaacademico" ("id")
)
;
CREATE TABLE "siscupos_estudiante" (
    "id" integer NOT NULL PRIMARY KEY,
    "codigo" integer NOT NULL,
    "nombres" varchar(200) NOT NULL,
    "apellidos" varchar(200) NOT NULL
)
;
CREATE TABLE "siscupos_asignaturaxestudiante" (
    "id" integer NOT NULL PRIMARY KEY,
    "cursada" varchar(2) NOT NULL,
    "estado" varchar(3) NOT NULL,
    "fechaAdicion" datetime NOT NULL,
    "fechaRemocion" datetime NOT NULL,
    "asignatura_id" integer NOT NULL REFERENCES "siscupos_asignatura" ("id"),
    "estudiante_id" integer NOT NULL REFERENCES "siscupos_estudiante" ("id")
)
;
CREATE TABLE "siscupos_preprogramacion" (
    "id" integer NOT NULL PRIMARY KEY,
    "seccion" integer NOT NULL,
    "cupos" integer NOT NULL,
    "diaSemana" varchar(1) NOT NULL,
    "periodo" varchar(10) NOT NULL,
    "asignaturaXPrograma_id" integer NOT NULL REFERENCES "siscupos_asignaturaxprograma" ("id")
)
;
CREATE TABLE "siscupos_preasignacioncurso" (
    "id" integer NOT NULL PRIMARY KEY,
    "codigo" integer NOT NULL,
    "fechaCorrida" datetime NOT NULL,
    "observacion" varchar(200) NOT NULL,
    "periodo" varchar(10) NOT NULL
)
;
CREATE TABLE "siscupos_asignaturasugerida" (
    "id" integer NOT NULL PRIMARY KEY,
    "anno" integer NOT NULL,
    "estado" varchar(10) NOT NULL,
    "preProgramacion_id" integer NOT NULL REFERENCES "siscupos_preprogramacion" ("id"),
    "estudiante_id" integer NOT NULL REFERENCES "siscupos_estudiante" ("id"),
    "preAsignacionCurso_id" integer NOT NULL REFERENCES "siscupos_preasignacioncurso" ("id")
)
;

COMMIT;