# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Series'
        db.delete_table('api_series')

        # Removing M2M table for field actors on 'Series'
        db.delete_table('api_series_actors')

        # Adding model 'FilmSet'
        db.create_table('api_filmset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['FilmSet'])

        # Adding model 'Show'
        db.create_table('api_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['Show'])

        # Adding M2M table for field actors on 'Show'
        db.create_table('api_show_actors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['api.show'], null=False)),
            ('actor', models.ForeignKey(orm['api.actor'], null=False))
        ))
        db.create_unique('api_show_actors', ['show_id', 'actor_id'])

        # Adding field 'Film.film_set'
        db.add_column('api_film', 'film_set',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['api.FilmSet']),
                      keep_default=False)


        # Changing field 'Episode.series'
        db.alter_column('api_episode', 'series_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Show']))

    def backwards(self, orm):
        # Adding model 'Series'
        db.create_table('api_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['Series'])

        # Adding M2M table for field actors on 'Series'
        db.create_table('api_series_actors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('series', models.ForeignKey(orm['api.series'], null=False)),
            ('actor', models.ForeignKey(orm['api.actor'], null=False))
        ))
        db.create_unique('api_series_actors', ['series_id', 'actor_id'])

        # Deleting model 'FilmSet'
        db.delete_table('api_filmset')

        # Deleting model 'Show'
        db.delete_table('api_show')

        # Removing M2M table for field actors on 'Show'
        db.delete_table('api_show_actors')

        # Deleting field 'Film.film_set'
        db.delete_column('api_film', 'film_set_id')


        # Changing field 'Episode.series'
        db.alter_column('api_episode', 'series_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Series']))

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
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Show']"})
        },
        'api.film': {
            'Meta': {'object_name': 'Film', '_ormbases': ['api.Content']},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Actor']", 'symmetrical': 'False'}),
            'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'film_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.FilmSet']"})
        },
        'api.filmset': {
            'Meta': {'object_name': 'FilmSet'},
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