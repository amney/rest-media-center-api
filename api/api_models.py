__author__ = 'tigarner'
from itertools import chain
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from api.models import Film, Episode, Content, Series, Actor


class SeriesResource(ModelResource):
    episodes = fields.ToManyField('api.api_models.EpisodeResource', 'episode_set')

    class Meta:
        queryset = Series.objects.all()
        authorization = Authorization()
        always_return_data = True


class FilmResource(ModelResource):
    class Meta:
        queryset = Film.objects.all()
        authorization = Authorization()
        always_return_data = True


class EpisodeResource(ModelResource):
    series = fields.ForeignKey(SeriesResource, 'series')

    class Meta:
        queryset = Episode.objects.all()
        authorization = Authorization()
        always_return_data = True


class ContentResource(ModelResource):
    film = fields.ForeignKey('api.api_models.ContentResource', 'film')

    class Meta:
        f = Film.objects.all()
        e = Episode.objects.all()
        c = list(chain(f,e))
        queryset = c
        authorization = Authorization()
        always_return_data = True


class ActorResource(ModelResource):
    class Meta:
        queryset = Actor.objects.all()
        authorization = Authorization()
        always_return_data = True