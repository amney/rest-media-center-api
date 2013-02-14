# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.status'
        db.add_column('api_player', 'status',
                      self.gf('django.db.models.fields.CharField')(default='stopped', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.status'
        db.delete_column('api_player', 'status')


    models = {
        'api.actor': {
            'Meta': {'object_name': 'Actor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'api.content': {
            'Meta': {'object_name': 'Content'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'api.episode': {
            'Meta': {'object_name': 'Episode', '_ormbases': ['api.Content']},
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Series']"})
        },
        'api.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['api.Content']},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Actor']", 'symmetrical': 'False'}),
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'})
        },
        'api.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Playlist']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'stopped'", 'max_length': '50'})
        },
        'api.playlist': {
            'Meta': {'object_name': 'Playlist'},
            'content': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Content']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'api.series': {
            'Meta': {'object_name': 'Series'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Actor']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']