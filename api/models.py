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

