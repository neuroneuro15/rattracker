# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rat'
        db.create_table(u'ratlog_rat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('strain', self.gf('django.db.models.fields.CharField')(default='Long Evans', max_length=30)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('protocol', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Rat'])

        # Adding model 'Cage'
        db.create_table(u'ratlog_cage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('cage', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ratlog', ['Cage'])

        # Adding model 'Task'
        db.create_table(u'ratlog_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('maze_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Task'])

        # Adding model 'Session'
        db.create_table(u'ratlog_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 28, 0, 0))),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Task'])),
            ('task_learned', self.gf('django.db.models.fields.BooleanField')()),
            ('motivation', self.gf('django.db.models.fields.FloatField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Session'])

        # Adding model 'Weight'
        db.create_table(u'ratlog_weight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Session'])),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Weight'])

        # Adding model 'Water'
        db.create_table(u'ratlog_water', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Session'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 28, 0, 0))),
            ('context', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Water'])

        # Adding model 'Drug'
        db.create_table(u'ratlog_drug', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ratlog', ['Drug'])

        # Adding model 'Medication'
        db.create_table(u'ratlog_medication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('drug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Drug'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 28, 0, 0))),
            ('dose', self.gf('django.db.models.fields.FloatField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('name', self.gf('django.db.models.fields.FloatField')()),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'ratlog', ['Medication'])

        # Adding model 'Vital'
        db.create_table(u'ratlog_vital', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 28, 0, 0))),
            ('heart_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Vital'])


    def backwards(self, orm):
        # Deleting model 'Rat'
        db.delete_table(u'ratlog_rat')

        # Deleting model 'Cage'
        db.delete_table(u'ratlog_cage')

        # Deleting model 'Task'
        db.delete_table(u'ratlog_task')

        # Deleting model 'Session'
        db.delete_table(u'ratlog_session')

        # Deleting model 'Weight'
        db.delete_table(u'ratlog_weight')

        # Deleting model 'Water'
        db.delete_table(u'ratlog_water')

        # Deleting model 'Drug'
        db.delete_table(u'ratlog_drug')

        # Deleting model 'Medication'
        db.delete_table(u'ratlog_medication')

        # Deleting model 'Vital'
        db.delete_table(u'ratlog_vital')


    models = {
        u'ratlog.cage': {
            'Meta': {'object_name': 'Cage'},
            'cage': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"})
        },
        u'ratlog.drug': {
            'Meta': {'object_name': 'Drug'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ratlog.medication': {
            'Meta': {'object_name': 'Medication'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 28, 0, 0)'}),
            'dose': ('django.db.models.fields.FloatField', [], {}),
            'drug': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Drug']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.FloatField', [], {}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"})
        },
        u'ratlog.rat': {
            'Meta': {'object_name': 'Rat'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'strain': ('django.db.models.fields.CharField', [], {'default': "'Long Evans'", 'max_length': '30'})
        },
        u'ratlog.session': {
            'Meta': {'object_name': 'Session'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 28, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'motivation': ('django.db.models.fields.FloatField', [], {}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Task']"}),
            'task_learned': ('django.db.models.fields.BooleanField', [], {})
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
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 28, 0, 0)'}),
            'heart_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ratlog.water': {
            'Meta': {'object_name': 'Water'},
            'amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 28, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Session']"}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ratlog.weight': {
            'Meta': {'object_name': 'Weight'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Session']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['ratlog']