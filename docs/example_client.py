#!/usr/local/bin/python

__author__ = 'Tim Garner'
import slumber

api = slumber.API("http://api.tim-garner.co.uk/api/v1/")
shows = api.show.get()
print shows
show = api.show(1).get()
print show
episodes = api.show(1).episodes.get()
print episodes
show = api.show.get(name='Friends')
print shows
new_show = api.show.post({"name": "The Office UK"})
ep1 = api.episode.post(
    {"episode_number": "1", "season_number": "1", "length": "30:00", "name": "Downsize", "plot": "plot1",
     "show": new_show})
ep2 = api.episode.post(
    {"episode_number": "2", "season_number": "1", "length": "30:00", "name": "Work Experience", "plot": "plot2",
     "show": new_show})
ep3 = api.episode.post(
    {"episode_number": "3", "season_number": "1", "length": "30:00", "name": "The Quiz", "plot": "plot3",
     "show": new_show})
playlist = api.playlist.post({"name", "My favourite office episodes"})
playlist = api.playlist(playlist['id']).patch(
    {"content": [{"resource_uri": ep1}, {"resource_uri": ep2}, {"resource_uri": ep3}]})
print playlist
