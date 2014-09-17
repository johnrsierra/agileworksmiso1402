from django.db import models
from django.db.models import Count


class Asignatura(models.Model):
    codigo = models.CharField(max_length=20)
    nombres = models.CharField(max_length=200)
    creditos = models.IntegerField()
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
    def __unicode__(self):
        return unicode(self.codigo) + ' ' + unicode(self.nombres) + ' ' + unicode(self.apellidos)


class AsignaturaXEstudiante(models.Model):
    cursada = models.CharField(max_length=2)
    estado = models.CharField(max_length=3)
    fechaAdicion = models.DateTimeField()
    fechaRemocion = models.DateTimeField()
    asignatura = models.ForeignKey(Asignatura)
    estudiante = models.ForeignKey(Estudiante)
    def __unicode__(self):
        return unicode(self.estudiante) + ' ' + unicode(self.asignatura)


class PreProgramacion(models.Model):
    seccion = models.IntegerField()
    cupos = models.IntegerField()
    diaSemana = models.CharField(max_length=1)
    periodo = models.CharField(max_length=10)
    asignaturaXPrograma = models.ForeignKey(AsignaturaXPrograma)
    def __unicode__(self):
        return str(self.seccion) + ' ' + self.periodo + ' ' + unicode(self.asignaturaXPrograma)
    class Meta:
        verbose_name_plural = "Pre Programaciones"

class PreAsignacionCurso(models.Model):
    codigo = models.IntegerField(max_length=20)
    fechaCorrida = models.DateTimeField()
    observacion = models.CharField(max_length=200)
    periodo = models.CharField(max_length=10)
    def __unicode__(self):
        return self.codigo+' '+self.fechaCorrida+' '+self.periodo

#Clase Asignatura
class AsignaturaSugerida(models.Model):
    anno = models.IntegerField(max_length=4)
    estado = models.CharField(max_length=10)
    preProgramacion = models.ForeignKey(PreProgramacion)
    estudiante = models.ForeignKey(Estudiante)
    preAsignacionCurso = models.ForeignKey(PreAsignacionCurso)
    def __unicode__(self):
        return self.preAsignacionCurso.fechaCorrida
        #return unicode(self.anno) + ' ' + self.estado + ' ' + unicode(self.preProgramacion) + ' ' + unicode(self.estudiante) + ' ' + unicode(self.preAsignacionCurso)