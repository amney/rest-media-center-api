from collections import deque
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)


class Series(models.Model):
    name = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor)


class Content(models.Model):
    name = models.CharField(max_length=255)


class Episode(Content):
    series = models.ForeignKey(Series)


class Film(Content):
    actors = models.ManyToManyField(Actor)


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    content = models.ManyToManyField(Content)


class Player(models.Model):
    playlist = models.ForeignKey(Playlist)
    status = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        choices=
        (('playing', 'playing'),
         ('paused', 'paused'),
         ('stopped', 'stopped')),
        default='stopped'
    )

    def play(self):
        self.status = 'playing'
        self.save()

    def pause(self):
        self.status = 'paused'
        self.save()

    def stop(self):
        self.status = 'stopped'
        self.save()