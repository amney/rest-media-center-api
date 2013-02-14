__author__ = 'tigarner'
from tastypie.resources import ModelResource, Resource
from tastypie.authorization import Authorization
from tastypie import fields
from api.models import Film, Episode, Series, Actor, Playlist, Content, Player


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


class ActorResource(ModelResource):
    class Meta:
        queryset = Actor.objects.all()
        authorization = Authorization()
        always_return_data = True


class ContentResource(ModelResource):

    class Meta:
        queryset = Content.objects.all()


class PlaylistResource(ModelResource):
    content = fields.ToManyField(ContentResource, 'content', full=True)

    class Meta:
        queryset = Playlist.objects.all()
        authorization = Authorization()
        always_return_data = True


class PlayerResource(ModelResource):
    playlist = fields.ForeignKey(PlaylistResource, 'playlist')

    def get_object_list(self, request):
        action = request.GET.get('action', '')

        if action:
            player = Player.objects.get(pk=1)
            if action == 'play':
                player.play()
            elif action == 'pause':
                player.pause()
            elif action == 'stop':
                player.stop()
            elif action == 'forward':
                pass
            elif action == 'back':
                pass

        return ModelResource.get_object_list(self, request)

    class Meta:
        queryset = Player.objects.all()
