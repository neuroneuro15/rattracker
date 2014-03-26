# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Vitals'
        db.delete_table(u'ratlog_vitals')

        # Adding model 'Vital'
        db.create_table(u'ratlog_vital', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('heart_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Vital'])


    def backwards(self, orm):
        # Adding model 'Vitals'
        db.create_table(u'ratlog_vitals', (
            ('temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('heart_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ratlog', ['Vitals'])

        # Deleting model 'Vital'
        db.delete_table(u'ratlog_vital')


    models = {
        u'ratlog.behavior': {
            'Meta': {'object_name': 'Behavior'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'motivation': ('django.db.models.fields.FloatField', [], {}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Task']"}),
            'task_learned': ('django.db.models.fields.BooleanField', [], {})
        },
        u'ratlog.medication': {
            'Meta': {'object_name': 'Medication'},
            'amount': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"})
        },
        u'ratlog.rat': {
            'Meta': {'object_name': 'Rat'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            'strain': ('django.db.models.fields.CharField', [], {'default': "'Long Evans'", 'max_length': '30'})
        },
        u'ratlog.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maze_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ratlog.vital': {
            'Meta': {'object_name': 'Vital'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            'heart_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ratlog.water': {
            'Meta': {'object_name': 'Water'},
            'amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ratlog.weight': {
            'Meta': {'object_name': 'Weight'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['ratlog']