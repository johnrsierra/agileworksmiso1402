# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AsignaturaXEstudiante.fechaAdicion'
        db.delete_column(u'siscupos_asignaturaxestudiante', 'fechaAdicion')

        # Deleting field 'AsignaturaXEstudiante.fechaRemocion'
        db.delete_column(u'siscupos_asignaturaxestudiante', 'fechaRemocion')

        # Adding field 'AsignaturaXEstudiante.periodo'
        db.add_column(u'siscupos_asignaturaxestudiante', 'periodo',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=6),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'AsignaturaXEstudiante.fechaAdicion'
        raise RuntimeError("Cannot reverse this migration. 'AsignaturaXEstudiante.fechaAdicion' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'AsignaturaXEstudiante.fechaAdicion'
        db.add_column(u'siscupos_asignaturaxestudiante', 'fechaAdicion',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'AsignaturaXEstudiante.fechaRemocion'
        raise RuntimeError("Cannot reverse this migration. 'AsignaturaXEstudiante.fechaRemocion' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'AsignaturaXEstudiante.fechaRemocion'
        db.add_column(u'siscupos_asignaturaxestudiante', 'fechaRemocion',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Deleting field 'AsignaturaXEstudiante.periodo'
        db.delete_column(u'siscupos_asignaturaxestudiante', 'periodo')


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