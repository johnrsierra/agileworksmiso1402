# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Asignatura'
        db.create_table(u'siscupos_asignatura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('creditos', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'siscupos', ['Asignatura'])

        # Adding model 'ProgramaAcademico'
        db.create_table(u'siscupos_programaacademico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombreCoordinador', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'siscupos', ['ProgramaAcademico'])

        # Adding model 'AsignaturaXPrograma'
        db.create_table(u'siscupos_asignaturaxprograma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('esefectivo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('semestresugerido', self.gf('django.db.models.fields.IntegerField')()),
            ('creditosPrerequisitos', self.gf('django.db.models.fields.IntegerField')()),
            ('asignatura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.Asignatura'])),
            ('programaAcademico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.ProgramaAcademico'])),
        ))
        db.send_create_signal(u'siscupos', ['AsignaturaXPrograma'])

        # Adding model 'Estudiante'
        db.create_table(u'siscupos_estudiante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.IntegerField')(max_length=20)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'siscupos', ['Estudiante'])

        # Adding model 'AsignaturaXEstudiante'
        db.create_table(u'siscupos_asignaturaxestudiante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cursada', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('fechaAdicion', self.gf('django.db.models.fields.DateTimeField')()),
            ('fechaRemocion', self.gf('django.db.models.fields.DateTimeField')()),
            ('asignatura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.Asignatura'])),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.Estudiante'])),
        ))
        db.send_create_signal(u'siscupos', ['AsignaturaXEstudiante'])

        # Adding model 'PreProgramacion'
        db.create_table(u'siscupos_preprogramacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seccion', self.gf('django.db.models.fields.IntegerField')()),
            ('cupos', self.gf('django.db.models.fields.IntegerField')()),
            ('diaSemana', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('periodo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('asignaturaXPrograma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.AsignaturaXPrograma'])),
        ))
        db.send_create_signal(u'siscupos', ['PreProgramacion'])

        # Adding model 'PreAsignacionCurso'
        db.create_table(u'siscupos_preasignacioncurso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.IntegerField')(max_length=20)),
            ('fechaCorrida', self.gf('django.db.models.fields.DateTimeField')()),
            ('observacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('periodo', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'siscupos', ['PreAsignacionCurso'])

        # Adding model 'AsignaturaSugerida'
        db.create_table(u'siscupos_asignaturasugerida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anno', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('preProgramacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.PreProgramacion'])),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.Estudiante'])),
            ('preAsignacionCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.PreAsignacionCurso'])),
        ))
        db.send_create_signal(u'siscupos', ['AsignaturaSugerida'])


    def backwards(self, orm):
        # Deleting model 'Asignatura'
        db.delete_table(u'siscupos_asignatura')

        # Deleting model 'ProgramaAcademico'
        db.delete_table(u'siscupos_programaacademico')

        # Deleting model 'AsignaturaXPrograma'
        db.delete_table(u'siscupos_asignaturaxprograma')

        # Deleting model 'Estudiante'
        db.delete_table(u'siscupos_estudiante')

        # Deleting model 'AsignaturaXEstudiante'
        db.delete_table(u'siscupos_asignaturaxestudiante')

        # Deleting model 'PreProgramacion'
        db.delete_table(u'siscupos_preprogramacion')

        # Deleting model 'PreAsignacionCurso'
        db.delete_table(u'siscupos_preasignacioncurso')

        # Deleting model 'AsignaturaSugerida'
        db.delete_table(u'siscupos_asignaturasugerida')


    models = {
        u'siscupos.asignatura': {
            'Meta': {'object_name': 'Asignatura'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'creditos': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'siscupos.asignaturasugerida': {
            'Meta': {'object_name': 'AsignaturaSugerida'},
            'anno': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.Estudiante']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preAsignacionCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.PreAsignacionCurso']"}),
            'preProgramacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.PreProgramacion']"})
        },
        u'siscupos.asignaturaxestudiante': {
            'Meta': {'object_name': 'AsignaturaXEstudiante'},
            'asignatura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.Asignatura']"}),
            'cursada': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.Estudiante']"}),
            'fechaAdicion': ('django.db.models.fields.DateTimeField', [], {}),
            'fechaRemocion': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'siscupos.asignaturaxprograma': {
            'Meta': {'object_name': 'AsignaturaXPrograma'},
            'asignatura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.Asignatura']"}),
            'creditosPrerequisitos': ('django.db.models.fields.IntegerField', [], {}),
            'esefectivo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programaAcademico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.ProgramaAcademico']"}),
            'semestresugerido': ('django.db.models.fields.IntegerField', [], {})
        },
        u'siscupos.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'codigo': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'siscupos.preasignacioncurso': {
            'Meta': {'object_name': 'PreAsignacionCurso'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            'fechaCorrida': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'siscupos.preprogramacion': {
            'Meta': {'object_name': 'PreProgramacion'},
            'asignaturaXPrograma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.AsignaturaXPrograma']"}),
            'cupos': ('django.db.models.fields.IntegerField', [], {}),
            'diaSemana': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'seccion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'siscupos.programaacademico': {
            'Meta': {'object_name': 'ProgramaAcademico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombreCoordinador': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['siscupos']