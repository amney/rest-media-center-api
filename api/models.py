from django.db import models


class Actor(models.Model):
    '''
    Object representing an Actor in the Database.
    '''
    name = models.CharField(max_length=255)


class FilmSeries(models.Model):
    '''
    Object representing a FilmSeries in the Database.
    '''
    name = models.CharField(max_length=255)


class Show(models.Model):
    '''
    Object representing a Show in the Database.
    '''
    name = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor)


class Content(models.Model):
    '''
    Object representing a piece of Content in the Database.
    '''
    name = models.CharField(max_length=255)
    length = models.CharField(max_length=50)
    file_type = models.CharField(max_length=50, choices=(('mkv', 'mkv'), ('mp4', 'mp4'), ('avi', 'avi')))
    quality = models.CharField(max_length=50, choices=(('HDTV', 'HDTV'), ('TV', 'TV'), ('Blu-Ray', 'Blu-Ray')))
    frame_rate = models.PositiveIntegerField()



class Episode(Content):
    '''
    Object representing an Episode in the Database.
    '''
    show = models.ForeignKey(Show)


class Film(Content):
    '''
    Object representing a Film in the Database.
    '''
    actors = models.ManyToManyField(Actor)
    film_series = models.ForeignKey(FilmSeries, null=True, blank=True)


class Playlist(models.Model):
    '''
    Object representing a Playlist in the Database.
    '''
    name = models.CharField(max_length=255)
    content = models.ManyToManyField(Content)


class Player(models.Model):
    '''
    Object representing the Player in the Database.
    '''
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
        '''
        Play the current piece of content in the playlist
        '''
        self.status = 'playing'
        self.save()

    def pause(self):
        '''
        Pause the current piece of content in the playlist
        '''
        self.status = 'paused'
        self.save()

    def stop(self):
        '''
        Stop the current piece of content in the playlist
        '''
        self.status = 'stopped'
        self.save()