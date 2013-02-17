# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FilmSeries.description'
        db.add_column('api_filmseries', 'description',
                      self.gf('django.db.models.fields.TextField')(default='default'),
                      keep_default=False)

        # Adding field 'Episode.season'
        db.add_column('api_episode', 'season',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Episode.episode_number'
        db.add_column('api_episode', 'episode_number',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Content.length'
        db.add_column('api_content', 'length',
                      self.gf('django.db.models.fields.CharField')(default='1:00', max_length=50),
                      keep_default=False)

        # Adding field 'Content.file_type'
        db.add_column('api_content', 'file_type',
                      self.gf('django.db.models.fields.CharField')(default='mkv', max_length=50),
                      keep_default=False)

        # Adding field 'Content.quality'
        db.add_column('api_content', 'quality',
                      self.gf('django.db.models.fields.CharField')(default='HDTV', max_length=50),
                      keep_default=False)

        # Adding field 'Content.frame_rate'
        db.add_column('api_content', 'frame_rate',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=24),
                      keep_default=False)

        # Adding field 'Content.plot'
        db.add_column('api_content', 'plot',
                      self.gf('django.db.models.fields.TextField')(default='default'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FilmSeries.description'
        db.delete_column('api_filmseries', 'description')

        # Deleting field 'Episode.season'
        db.delete_column('api_episode', 'season')

        # Deleting field 'Episode.episode_number'
        db.delete_column('api_episode', 'episode_number')

        # Deleting field 'Content.length'
        db.delete_column('api_content', 'length')

        # Deleting field 'Content.file_type'
        db.delete_column('api_content', 'file_type')

        # Deleting field 'Content.quality'
        db.delete_column('api_content', 'quality')

        # Deleting field 'Content.frame_rate'
        db.delete_column('api_content', 'frame_rate')

        # Deleting field 'Content.plot'
        db.delete_column('api_content', 'plot')


    models = {
        'api.actor': {
            'Meta': {'object_name': 'Actor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'api.content': {
            'Meta': {'object_name': 'Content'},
            'file_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'frame_rate': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'plot': ('django.db.models.fields.TextField', [], {}),
            'quality': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'api.episode': {
            'Meta': {'object_name': 'Episode', '_ormbases': ['api.Content']},
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'episode_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'season': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Show']"})
        },
        'api.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['api.Content']},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Actor']", 'symmetrical': 'False'}),
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'film_series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.FilmSeries']", 'null': 'True', 'blank': 'True'})
        },
        'api.filmseries': {
            'Meta': {'object_name': 'FilmSeries'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        'api.show': {
            'Meta': {'object_name': 'Show'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Actor']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']