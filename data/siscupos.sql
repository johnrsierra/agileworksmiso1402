BEGIN;
CREATE TABLE "siscupos_asignatura" (
    "id" serial NOT NULL PRIMARY KEY,
    "codigo" varchar(20) NOT NULL,
    "nombres" varchar(200) NOT NULL,
    "creditos" integer NOT NULL
)
;
CREATE TABLE "siscupos_programaacademico" (
    "id" serial NOT NULL PRIMARY KEY,
    "sigla" varchar(10) NOT NULL,
    "nombre" varchar(200) NOT NULL,
    "nombreCoordinador" varchar(200) NOT NULL
)
;
CREATE TABLE "siscupos_asignaturaxprograma" (
    "id" serial NOT NULL PRIMARY KEY,
    "esefectivo" varchar(2) NOT NULL,
    "semestresugerido" integer NOT NULL,
    "creditosPrerequisitos" integer NOT NULL,
    "asignatura_id" integer NOT NULL REFERENCES "siscupos_asignatura" ("id") DEFERRABLE INITIALLY DEFERRED,
    "programaAcademico_id" integer NOT NULL REFERENCES "siscupos_programaacademico" ("id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "siscupos_estudiante" (
    "id" serial NOT NULL PRIMARY KEY,
    "codigo" integer NOT NULL,
    "nombres" varchar(200) NOT NULL,
    "apellidos" varchar(200) NOT NULL
)
;
CREATE TABLE "siscupos_asignaturaxestudiante" (
    "id" serial NOT NULL PRIMARY KEY,
    "cursada" varchar(2) NOT NULL,
    "estado" varchar(3) NOT NULL,
    "fechaAdicion" timestamp with time zone NOT NULL,
    "fechaRemocion" timestamp with time zone NOT NULL,
    "asignatura_id" integer NOT NULL REFERENCES "siscupos_asignatura" ("id") DEFERRABLE INITIALLY DEFERRED,
    "estudiante_id" integer NOT NULL REFERENCES "siscupos_estudiante" ("id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "siscupos_preprogramacion" (
    "id" serial NOT NULL PRIMARY KEY,
    "seccion" integer NOT NULL,
    "cupos" integer NOT NULL,
    "diaSemana" varchar(1) NOT NULL,
    "periodo" varchar(10) NOT NULL,
    "asignaturaXPrograma_id" integer NOT NULL REFERENCES "siscupos_asignaturaxprograma" ("id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "siscupos_preasignacioncurso" (
    "id" serial NOT NULL PRIMARY KEY,
    "codigo" integer NOT NULL,
    "fechaCorrida" timestamp with time zone NOT NULL,
    "observacion" varchar(200) NOT NULL,
    "periodo" varchar(10) NOT NULL
)
;
CREATE TABLE "siscupos_asignaturasugerida" (
    "id" serial NOT NULL PRIMARY KEY,
    "anno" integer NOT NULL,
    "estado" varchar(10) NOT NULL,
    "preProgramacion_id" integer NOT NULL REFERENCES "siscupos_preprogramacion" ("id") DEFERRABLE INITIALLY DEFERRED,
    "estudiante_id" integer NOT NULL REFERENCES "siscupos_estudiante" ("id") DEFERRABLE INITIALLY DEFERRED,
    "preAsignacionCurso_id" integer NOT NULL REFERENCES "siscupos_preasignacioncurso" ("id") DEFERRABLE INITIALLY DEFERRED
)
;

COMMIT;