from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)


class FilmSeries(models.Model):
    name = models.CharField(max_length=255)


class Show(models.Model):
    name = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor)


class Content(models.Model):
    name = models.CharField(max_length=255)


class Episode(Content):
    show = models.ForeignKey(Show)


class Film(Content):
    actors = models.ManyToManyField(Actor)
    film_series = models.ForeignKey(FilmSeries, null=True, blank=True)


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