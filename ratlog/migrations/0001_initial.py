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
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('strain', self.gf('django.db.models.fields.CharField')(default='Long Evans', max_length=30)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('protocol', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Rat'])

        # Adding model 'Weight'
        db.create_table(u'ratlog_weight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Weight'])

        # Adding model 'Water'
        db.create_table(u'ratlog_water', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('amount', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('time', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('context', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'ratlog', ['Water'])

        # Adding model 'Medication'
        db.create_table(u'ratlog_medication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Medication'])

        # Adding model 'Vitals'
        db.create_table(u'ratlog_vitals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratlog.Rat'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 26, 0, 0))),
            ('heart_rate', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'ratlog', ['Vitals'])


    def backwards(self, orm):
        # Deleting model 'Rat'
        db.delete_table(u'ratlog_rat')

        # Deleting model 'Weight'
        db.delete_table(u'ratlog_weight')

        # Deleting model 'Water'
        db.delete_table(u'ratlog_water')

        # Deleting model 'Medication'
        db.delete_table(u'ratlog_medication')

        # Deleting model 'Vitals'
        db.delete_table(u'ratlog_vitals')


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
        u'ratlog.vitals': {
            'Meta': {'object_name': 'Vitals'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            'heart_rate': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'temperature': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        u'ratlog.water': {
            'Meta': {'object_name': 'Water'},
            'amount': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratlog.Rat']"}),
            'time': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
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