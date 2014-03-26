# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Behavior'
        db.delete_table(u'ratlog_behavior')

        # Deleting model 'Water'
        db.delete_table(u'ratlog_water')

        # Adding model 'Session'
        db.create_table(u'ratlog_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Task'])),
            ('task_learned', self.gf('django.db.models.fields.BooleanField')()),
            ('motivation', self.gf('django.db.models.fields.FloatField')()),
            ('water_context', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('water_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('water_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Session'])


    def backwards(self, orm):
        # Adding model 'Behavior'
        db.create_table(u'ratlog_behavior', (
            ('motivation', self.gf('django.db.models.fields.FloatField')()),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Task'])),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('task_learned', self.gf('django.db.models.fields.BooleanField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
        ))
        db.send_create_signal(u'ratlog', ['Behavior'])

        # Adding model 'Water'
        db.create_table(u'ratlog_water', (
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('context', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ratlog', ['Water'])

        # Deleting model 'Session'
        db.delete_table(u'ratlog_session')


    models = {
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
        u'ratlog.session': {
            'Meta': {'object_name': 'Session'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'motivation': ('django.db.models.fields.FloatField', [], {}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Task']"}),
            'task_learned': ('django.db.models.fields.BooleanField', [], {}),
            'water_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water_context': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'water_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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