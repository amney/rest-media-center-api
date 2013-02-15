from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.resources import ALL_WITH_RELATIONS

__author__ = 'tigarner'
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from api.models import Film, Episode, Show, Actor, Playlist, Content, Player, FilmSeries


class EpisodeResource(ModelResource):
    show = fields.ForeignKey('api.api_models.ShowResource', 'show')

    class Meta:
        queryset = Episode.objects.all()
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'show': ALL_WITH_RELATIONS,
            }


class ShowResource(ModelResource):
    episodes = fields.ToManyField('api.api_models.EpisodeResource', 'episode_set', null=True)

    def prepend_urls(self):
        '''
        Note to self prepend_urls needs tastypie version 0.9.12 >=
        '''

        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/episodes%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_children'), name="api_get_children"),]

    def get_children(self, request, **kwargs):
        child_resource = EpisodeResource()
        return child_resource.get_list(request, show=kwargs.pop('pk'))

    class Meta:
        queryset = Show.objects.all()
        authorization = Authorization()
        always_return_data = True
        resource_name = 'show'


class FilmSeriesResource(ModelResource):
    films = fields.ToManyField('api.api_models.FilmResource', 'film_set', null=True, full=True)

    def prepend_urls(self):
        '''
        Note to self prepend_urls needs tastypie version 0.9.12 >=
        '''

        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/films%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_children'), name="api_get_children"),]

    def get_children(self, request, **kwargs):
        child_resource = FilmResource()
        return child_resource.get_list(request, film_series=kwargs.pop('pk'))

    class Meta:
        queryset = FilmSeries.objects.all()
        authorization = Authorization()
        always_return_data = True


class FilmResource(ModelResource):
    film_series = fields.ForeignKey(FilmSeriesResource, 'film_series', null=True)

    class Meta:
        queryset = Film.objects.all()
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'film_series': ALL_WITH_RELATIONS,
            }


class ActorResource(ModelResource):
    class Meta:
        queryset = Actor.objects.all()
        authorization = Authorization()
        always_return_data = True


class ContentResource(ModelResource):

    class Meta:
        queryset = Content.objects.all()
        authorization = Authorization()
        always_return_data = True

class PlaylistResource(ModelResource):
    content = fields.ToManyField(ContentResource, 'content', null=True, full=True)

    class Meta:
        queryset = Playlist.objects.all()
        authorization = Authorization()
        always_return_data = True


class PlayerResource(ModelResource):
    '''
    Represents the media player, takes actions to control the playback of media.
    The 'list' url is overriden to just return one player object as that's all there is!
    '''

    playlist = fields.ForeignKey(PlaylistResource, 'playlist')

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('player'), name="api_player"), ]

    def player(self, request, **kwargs):
        player = PlayerResource()

        action = request.GET.get('action', '')

        if action:
            player_obj = Player.objects.get(pk=1)
            if action == 'play':
                player_obj.play()
            elif action == 'pause':
                player_obj.pause()
            elif action == 'stop':
                player_obj.stop()
            elif action == 'forward':
                pass
            elif action == 'back':
                pass

        return player.get_detail(request, id=1)

    class Meta:
        queryset = Player.objects.all()
