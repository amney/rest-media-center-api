from django.db import models
from datetime import date, datetime


class Actor(models.Model):
    '''
    Object representing an Actor in the Database.
    '''
    name = models.CharField(max_length=255, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False, default=date(1990, 07, 19))
    bio = models.TextField(null=False, blank=True)

    def __unicode__(self):
        return self.name


class FilmSeries(models.Model):
    '''
    Object representing a FilmSeries in the Database.
    '''
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Film Series'
        verbose_name = 'Film Series'


class Show(models.Model):
    '''
    Object representing a Show in the Database.
    '''
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    actors = models.ManyToManyField(Actor, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Content(models.Model):
    '''
    Object representing a piece of Content in the Database.
    '''
    name = models.CharField(max_length=255, null=False, blank=False)
    length = models.CharField(max_length=50, null=False, blank=False,
                              help_text='Content length represented in string form, for example 30:00')
    file_type = models.CharField(max_length=50, null=False, default='mkv',
                                 choices=(('mkv', 'mkv'), ('mp4', 'mp4'), ('avi', 'avi')),
                                 help_text='Choice of either mkv, mp4 or avi')
    quality = models.CharField(max_length=50, null=False, default='TV',
                               choices=(('HDTV', 'HDTV'), ('TV', 'TV'), ('Blu-Ray', 'Blu-Ray')),
                               help_text='Choice of either HDTV, TV or Blu-Ray')
    frame_rate = models.PositiveIntegerField(null=False, blank=False, default=60)
    plot = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Episode(Content):
    '''
    Object representing an Episode in the Database.
    '''
    show = models.ForeignKey(Show)
    season = models.PositiveIntegerField(default=1, null=False, blank=False)
    episode_number = models.PositiveIntegerField(default=1, null=False, blank=False)

    class Meta:
        unique_together = ('season', 'episode_number', 'show')


class Film(Content):
    '''
    Object representing a Film in the Database.
    '''
    actors = models.ManyToManyField(Actor, null=True, blank=True)
    film_series = models.ForeignKey(FilmSeries, null=True, blank=True)
    release_date = models.DateField(null=False, blank=False, default=date(1990, 07, 19))


class Playlist(models.Model):
    '''
    Object representing a Playlist in the Database.
    '''
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    content = models.ManyToManyField(Content, null=True, blank=False)
    auto_create_time = models.DateTimeField(auto_now_add=True, null=False, blank=False, default=datetime.utcnow())
    auto_modify_time = models.DateTimeField(auto_now=True, null=False, blank=False, default=datetime.utcnow())

    def __unicode__(self):
        return self.name


class Player(models.Model):
    '''
    Object representing the Player in the Database.
    '''
    playlist = models.ForeignKey(Playlist, null=True, blank=False)
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

    def next(self):
        '''
        Go to the next piece of content in the playlist
        '''
        #Pretend to go to the next item in the playlist
        pass

    def back(self):
        '''
        Go to the previous piece of content in the playlist
        '''
        #Pretend to go to the previous item in the playlist
        pass

    def __unicode__(self):
        return 'Media Player'