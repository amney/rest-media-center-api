# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Actor'
        db.create_table('api_actor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['Actor'])

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

        # Adding model 'Content'
        db.create_table('api_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['Content'])

        # Adding model 'Episode'
        db.create_table('api_episode', (
            ('content_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['api.Content'], unique=True, primary_key=True)),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Series'])),
        ))
        db.send_create_signal('api', ['Episode'])

        # Adding model 'Film'
        db.create_table('api_film', (
            ('content_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['api.Content'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('api', ['Film'])

        # Adding M2M table for field actors on 'Film'
        db.create_table('api_film_actors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['api.film'], null=False)),
            ('actor', models.ForeignKey(orm['api.actor'], null=False))
        ))
        db.create_unique('api_film_actors', ['film_id', 'actor_id'])

        # Adding model 'Playlist'
        db.create_table('api_playlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['Playlist'])

        # Adding M2M table for field content on 'Playlist'
        db.create_table('api_playlist_content', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('playlist', models.ForeignKey(orm['api.playlist'], null=False)),
            ('content', models.ForeignKey(orm['api.content'], null=False))
        ))
        db.create_unique('api_playlist_content', ['playlist_id', 'content_id'])

        # Adding model 'Player'
        db.create_table('api_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('playlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Playlist'])),
        ))
        db.send_create_signal('api', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Actor'
        db.delete_table('api_actor')

        # Deleting model 'Series'
        db.delete_table('api_series')

        # Removing M2M table for field actors on 'Series'
        db.delete_table('api_series_actors')

        # Deleting model 'Content'
        db.delete_table('api_content')

        # Deleting model 'Episode'
        db.delete_table('api_episode')

        # Deleting model 'Film'
        db.delete_table('api_film')

        # Removing M2M table for field actors on 'Film'
        db.delete_table('api_film_actors')

        # Deleting model 'Playlist'
        db.delete_table('api_playlist')

        # Removing M2M table for field content on 'Playlist'
        db.delete_table('api_playlist_content')

        # Deleting model 'Player'
        db.delete_table('api_player')


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
            'playlist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Playlist']"})
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