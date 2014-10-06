# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PreProgramacionAsig'
        db.create_table(u'siscupos_preprogramacionasig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seccion', self.gf('django.db.models.fields.IntegerField')()),
            ('cupos', self.gf('django.db.models.fields.IntegerField')()),
            ('diaSemana', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('periodo', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('asignaturaXPrograma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.AsignaturaXPrograma'])),
            ('preAsignacionCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siscupos.PreAsignacionCurso'])),
        ))
        db.send_create_signal(u'siscupos', ['PreProgramacionAsig'])


        # Changing field 'PreProgramacion.periodo'
        db.alter_column(u'siscupos_preprogramacion', 'periodo', self.gf('django.db.models.fields.CharField')(max_length=6))

        # Changing field 'PreAsignacionCurso.periodo'
        db.alter_column(u'siscupos_preasignacioncurso', 'periodo', self.gf('django.db.models.fields.CharField')(max_length=6))

    def backwards(self, orm):
        # Deleting model 'PreProgramacionAsig'
        db.delete_table(u'siscupos_preprogramacionasig')


        # Changing field 'PreProgramacion.periodo'
        db.alter_column(u'siscupos_preprogramacion', 'periodo', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'PreAsignacionCurso.periodo'
        db.alter_column(u'siscupos_preasignacioncurso', 'periodo', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        u'siscupos.asignatura': {
            'Meta': {'object_name': 'Asignatura'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'creditos': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
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
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'periodoInicio': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'siscupos.preasignacioncurso': {
            'Meta': {'object_name': 'PreAsignacionCurso'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            'fechaCorrida': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'siscupos.preprogramacion': {
            'Meta': {'object_name': 'PreProgramacion'},
            'asignaturaXPrograma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.AsignaturaXPrograma']"}),
            'cupos': ('django.db.models.fields.IntegerField', [], {}),
            'diaSemana': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'seccion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'siscupos.preprogramacionasig': {
            'Meta': {'object_name': 'PreProgramacionAsig'},
            'asignaturaXPrograma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.AsignaturaXPrograma']"}),
            'cupos': ('django.db.models.fields.IntegerField', [], {}),
            'diaSemana': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'preAsignacionCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['siscupos.PreAsignacionCurso']"}),
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