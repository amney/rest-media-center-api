#!/usr/local/bin/python
__author__ = 'Tim Garner'
import slumber

print 'Create slumber API object, with basic authentication'
api = slumber.API("http://api.tim-garner.co.uk/api/v1/", auth=('api', 'api'))

print 'Get and print all shows'
shows = api.show.get()
print shows

print 'Get and print the show with ID 1'
show = api.show(1).get()
print show

print 'Get and print the episodes for show with ID 1'
episodes = api.show(1).episodes.get()
print episodes

print 'Get all shows with name=Friends'
show = api.show.get(name='Friends')
print shows

print 'Post a new show with name "The Office UK"'
new_show = api.show.post({"name": "The Office UK"})
print new_show

print 'Post 3 episodes for the previously created show'
ep1 = api.episode.post(
    {"episode_number": "1", "season_number": "1", "length": "30:00", "name": "Downsize", "plot": "plot1",
     "show": new_show})
ep2 = api.episode.post(
    {"episode_number": "2", "season_number": "1", "length": "30:00", "name": "Work Experience", "plot": "plot2",
     "show": new_show})
ep3 = api.episode.post(
    {"episode_number": "3", "season_number": "1", "length": "30:00", "name": "The Quiz", "plot": "plot3",
     "show": new_show})

print 'Post a new playlist'
playlist = api.playlist.post({"name": "My favourite office episodes"})

print 'Patch the three new episodes into the playlist'
playlist = api.playlist(playlist['id']).patch(
    {"content": [{"resource_uri": ep1}, {"resource_uri": ep2}, {"resource_uri": ep3}]})
print playlist

print 'Cleanup after ourselves and delete the new playlist and show (cascading deletes related episodes)'
api.playlist(playlist['id']).delete()
api.show(new_show['id']).delete()


