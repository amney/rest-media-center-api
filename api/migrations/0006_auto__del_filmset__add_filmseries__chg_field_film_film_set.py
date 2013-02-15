# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FilmSet'
        db.delete_table('api_filmset')

        # Adding model 'FilmSeries'
        db.create_table('api_filmseries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['FilmSeries'])


        # Changing field 'Film.film_set'
        db.alter_column('api_film', 'film_set_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.FilmSeries'], null=True))

    def backwards(self, orm):
        # Adding model 'FilmSet'
        db.create_table('api_filmset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['FilmSet'])

        # Deleting model 'FilmSeries'
        db.delete_table('api_filmseries')


        # Changing field 'Film.film_set'
        db.alter_column('api_film', 'film_set_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.FilmSet'], null=True))

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
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Show']"})
        },
        'api.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['api.Content']},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Actor']", 'symmetrical': 'False'}),
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'film_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.FilmSeries']", 'null': 'True', 'blank': 'True'})
        },
        'api.filmseries': {
            'Meta': {'object_name': 'FilmSeries'},
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