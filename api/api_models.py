__author__ = 'tigarner'

from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.resources import ALL_WITH_RELATIONS
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from api.models import Film, Episode, Show, Actor, Playlist, Content, Player, FilmSeries


class ActorResource(ModelResource):
    '''
    An Actor is a person that can be tied to many content objects
    '''
    class Meta:
        queryset = Actor.objects.all()
        authorization = Authorization()
        always_return_data = True


class EpisodeResource(ModelResource):
    '''
    Resource endpoint for Episode. A episode has a resource_uri pointing to the parent show.
    '''
    show = fields.ForeignKey('api.api_models.ShowResource', 'show')

    class Meta:
        queryset = Episode.objects.all()
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'show': ALL_WITH_RELATIONS,
            }


class ShowResource(ModelResource):
    '''
    Resource endpoint for Show. A show is made up of one or more episodes. An example would be the 'The Simpsons'.
    Appending /episodes/ to the end of a detailed resource will show all episodes belonging to that resource.
    '''
    episodes = fields.ToManyField('api.api_models.EpisodeResource', 'actors', null=True)
    actors = fields.ToManyField(ActorResource, 'show_set', null=True)

    def prepend_urls(self):
        '''
        This is used to allow /episodes/ as a nested resource.
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
    '''
    Resource endpoint for FilmSeries. Film series can be made up on two of more films that are logically grouped
    together. An example would be the Lord of The Rings Trilogy.
    Appending /films/ to the end of a detailed resource will show all films belonging to that resource.
    '''
    films = fields.ToManyField('api.api_models.FilmResource', 'film_set', null=True)

    def prepend_urls(self):
        '''
        This is used to allow /films/ as a nested resource.
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
    '''
    Resource endpoint for all Films. If the film belongs to a film series it will have a resource_uri pointing to that
    series.
    '''
    film_series = fields.ForeignKey(FilmSeriesResource, 'film_series', null=True)
    actors = fields.ToManyField(ActorResource, 'actors', null=True)

    class Meta:
        queryset = Film.objects.all()
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'film_series': ALL_WITH_RELATIONS,
            }


class ContentResource(ModelResource):
    '''
    Content is sort of a 'meta' resource. It is used to represent everything that IS a piece of content.
    Pragmatically this translates into a resource that lists all Film and Episode objects.
    '''
    class Meta:
        queryset = Content.objects.all()
        authorization = Authorization()
        always_return_data = True

class PlaylistResource(ModelResource):
    '''
    Resource endpoint for Playlist. Has an array of 'content' objects. These could either be films or episodes.
    '''
    content = fields.ToManyField(ContentResource, 'content', null=True)

    class Meta:
        queryset = Playlist.objects.all()
        authorization = Authorization()
        always_return_data = True


class PlayerResource(ModelResource):
    '''
    Represents the media player, takes actions to control the playback of media.
    The 'list' url is overridden to just return one player object as that's all there is!
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
