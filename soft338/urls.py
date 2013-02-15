from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.api_models import FilmResource, EpisodeResource, ShowResource, ActorResource, \
    PlaylistResource, ContentResource, PlayerResource, FilmSeriesResource
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
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soft338.views.home', name='home'),
    # url(r'^soft338/', include('soft338.foo.urls')),

    url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
