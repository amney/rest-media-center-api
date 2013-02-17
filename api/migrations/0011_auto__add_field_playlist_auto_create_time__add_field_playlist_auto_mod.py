# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Playlist.auto_create_time'
        db.add_column('api_playlist', 'auto_create_time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 2, 16, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Playlist.auto_modify_time'
        db.add_column('api_playlist', 'auto_modify_time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 2, 16, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Film.release_date'
        db.add_column('api_film', 'release_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(1990, 7, 19, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Playlist.auto_create_time'
        db.delete_column('api_playlist', 'auto_create_time')

        # Deleting field 'Playlist.auto_modify_time'
        db.delete_column('api_playlist', 'auto_modify_time')

        # Deleting field 'Film.release_date'
        db.delete_column('api_film', 'release_date')


    models = {
        'api.actor': {
            'Meta': {'object_name': 'Actor'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(1990, 7, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'api.content': {
            'Meta': {'object_name': 'Content'},
            'file_type': ('django.db.models.fields.CharField', [], {'default': "'mkv'", 'max_length': '50'}),
            'frame_rate': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'plot': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'default': "'TV'", 'max_length': '50'})
        },
        'api.episode': {
            'Meta': {'unique_together': "(('season', 'episode_number', 'show'),)", 'object_name': 'Episode', '_ormbases': ['api.Content']},
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'episode_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'season': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Show']"})
        },
        'api.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['api.Content']},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['api.Actor']", 'null': 'True', 'blank': 'True'}),
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'film_series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.FilmSeries']", 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(1990, 7, 19, 0, 0)'})
        },
        'api.filmseries': {
            'Meta': {'object_name': 'FilmSeries'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'api.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Playlist']", 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'stopped'", 'max_length': '50'})
        },
        'api.playlist': {
            'Meta': {'object_name': 'Playlist'},
            'auto_create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'auto_modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Content']", 'null': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'api.show': {
            'Meta': {'object_name': 'Show'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['api.Actor']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['api']