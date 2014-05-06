# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DemoUser'
        db.create_table(u'demo_demouser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('created', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128, db_index=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'demo', ['DemoUser'])

        # Adding model 'DemoInfo'
        db.create_table(u'demo_demoinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('intValue', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('floatValue', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('decimalField', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=6, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.DemoUser'], null=True, db_column='user', blank=True)),
            ('isBoolean', self.gf('django.db.models.fields.BooleanField')()),
            ('textField', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dateTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 6, 0, 0), blank=True)),
        ))
        db.send_create_signal(u'demo', ['DemoInfo'])

        # Adding model 'DemoInfoTwo'
        db.create_table(u'demo_demoinfotwo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('demoInfo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.DemoInfo'], null=True, blank=True)),
            ('choices', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'demo', ['DemoInfoTwo'])

        # Adding model 'DemoInfoThree'
        db.create_table(u'demo_demoinfothree', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('demoInfoTwo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.DemoInfoTwo'], null=True, blank=True)),
        ))
        db.send_create_signal(u'demo', ['DemoInfoThree'])

        # Adding M2M table for field demoInfos on 'DemoInfoThree'
        m2m_table_name = db.shorten_name(u'demo_demoinfothree_demoInfos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('demoinfothree', models.ForeignKey(orm[u'demo.demoinfothree'], null=False)),
            ('demoinfo', models.ForeignKey(orm[u'demo.demoinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['demoinfothree_id', 'demoinfo_id'])


    def backwards(self, orm):
        # Deleting model 'DemoUser'
        db.delete_table(u'demo_demouser')

        # Deleting model 'DemoInfo'
        db.delete_table(u'demo_demoinfo')

        # Deleting model 'DemoInfoTwo'
        db.delete_table(u'demo_demoinfotwo')

        # Deleting model 'DemoInfoThree'
        db.delete_table(u'demo_demoinfothree')

        # Removing M2M table for field demoInfos on 'DemoInfoThree'
        db.delete_table(db.shorten_name(u'demo_demoinfothree_demoInfos'))


    models = {
        u'demo.demoinfo': {
            'Meta': {'object_name': 'DemoInfo'},
            'dateTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 6, 0, 0)', 'blank': 'True'}),
            'decimalField': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'blank': 'True'}),
            'floatValue': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intValue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'isBoolean': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'textField': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.DemoUser']", 'null': 'True', 'db_column': "'user'", 'blank': 'True'})
        },
        u'demo.demoinfothree': {
            'Meta': {'object_name': 'DemoInfoThree'},
            'demoInfoTwo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.DemoInfoTwo']", 'null': 'True', 'blank': 'True'}),
            'demoInfos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['demo.DemoInfo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'demo.demoinfotwo': {
            'Meta': {'object_name': 'DemoInfoTwo'},
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'demoInfo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo.DemoInfo']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'demo.demouser': {
            'Meta': {'ordering': "['email']", 'object_name': 'DemoUser'},
            'created': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['demo']