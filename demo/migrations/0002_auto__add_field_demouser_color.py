# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DemoUser.color'
        db.add_column(u'demo_demouser', 'color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DemoUser.color'
        db.delete_column(u'demo_demouser', 'color')


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
            'color': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
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