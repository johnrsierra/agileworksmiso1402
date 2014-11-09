from django.db import models
from django.db.models import Count


class Asignatura(models.Model):
    codigo = models.CharField(max_length=20)
    nombres = models.CharField(max_length=200)
    creditos = models.IntegerField()
    nivel = models.CharField(max_length=200)
    credito_prerrequisitos = models.IntegerField()
    def __unicode__(self):
        return self.codigo+' '+self.nombres
    @staticmethod
    def demanda_cupos():
        return Asignatura.objects.annotate(demanda=Count('asignaturaxestudiante'))#.filter(asignaturaxestudiante__cursada='0')


class ProgramaAcademico(models.Model):
    sigla = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    nombreCoordinador = models.CharField(max_length=200)
    def __unicode__(self):
        return self.sigla + ' ' + self.nombre
    class Meta:
        verbose_name_plural = "Programas Academicos"


class AsignaturaXPrograma(models.Model):
    esefectivo = models.CharField(max_length=2)
    semestresugerido = models.IntegerField()
    creditosPrerequisitos = models.IntegerField()
    asignatura = models.ForeignKey(Asignatura)
    programaAcademico = models.ForeignKey(ProgramaAcademico)
    def __unicode__(self):
        return unicode(self.asignatura) + ' ' + unicode(self.programaAcademico)


class Estudiante(models.Model):
    codigo = models.IntegerField(max_length=20)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    periodoInicio = models.CharField(max_length=6)
    programa = models.ForeignKey(ProgramaAcademico, null=True, blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' ' + unicode(self.nombres) + ' ' + unicode(self.apellidos)


class AsignaturaXEstudiante(models.Model):
    cursada = models.CharField(max_length=2)
    estado = models.CharField(max_length=3)
    periodo = models.CharField(max_length=6)
    asignatura = models.ForeignKey(Asignatura)
    estudiante = models.ForeignKey(Estudiante)
    def __unicode__(self):
        return unicode(self.estudiante) + ' ' + unicode(self.asignatura)


class PreProgramacion(models.Model):
    seccion = models.IntegerField()
    cupos = models.IntegerField()
    diaSemana = models.CharField(max_length=1)
    periodo = models.CharField(max_length=6)
    asignaturaXPrograma = models.ForeignKey(AsignaturaXPrograma)
    def __unicode__(self):
        return str(self.seccion) + ' ' + self.periodo + ' ' + unicode(self.asignaturaXPrograma)
    class Meta:
        verbose_name_plural = "Pre Programaciones"

class PreAsignacionCurso(models.Model):
    codigo = models.IntegerField(max_length=20)
    fechaCorrida = models.DateTimeField()
    observacion = models.CharField(max_length=200)
    periodo = models.CharField(max_length=6)
    def __unicode__(self):
        return str(self.codigo) + ' ' + str(self.observacion) + unicode(self.fechaCorrida)

#Clase Asignatura
class AsignaturaSugerida(models.Model):
    anno = models.IntegerField(max_length=4)
    estado = models.CharField(max_length=10)
    preProgramacion = models.ForeignKey(PreProgramacion)
    estudiante = models.ForeignKey(Estudiante)
    preAsignacionCurso = models.ForeignKey(PreAsignacionCurso)
    def __unicode__(self):
        return unicode(self.preAsignacionCurso.fechaCorrida)

#Clase solicitada por FViera
class PreProgramacionAsig(models.Model):
    seccion = models.IntegerField()
    cupos = models.IntegerField()
    diaSemana = models.CharField(max_length=1)
    periodo = models.CharField(max_length=6)
    asignaturaXPrograma = models.ForeignKey(AsignaturaXPrograma)
    preAsignacionCurso = models.ForeignKey(PreAsignacionCurso)
