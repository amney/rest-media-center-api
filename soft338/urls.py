from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.api_models import *
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(FilmResource())
v1_api.register(EpisodeResource())
v1_api.register(ShowResource())
v1_api.register(ActorResource())
v1_api.register(ContentResource())
v1_api.register(PlaylistResource())
v1_api.register(PlayerResource())
v1_api.register(FilmSeriesResource())
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','api.views.home')
)
