__author__ = 'tigarner'
from django.contrib import admin
from api.models import *

admin.site.register(Actor)
admin.site.register(Film)
admin.site.register(FilmSeries)
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Playlist)
admin.site.register(Player)