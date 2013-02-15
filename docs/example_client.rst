Example Client
==============

For this example we will be using the Python library `Slumber <http://slumber.readthedocs.org/en/latest/>`_, an excellent
command line client designed for interacting with RESTful webservices.

While this guide has been written for python users, it should be easily followed in most other programming languages.

The path we will be following is:
    - `Setup the client`_
    - `List all TV shows, drill down a bit deeper for a particular show`_
    - `Create a new TV show`_
    - `Create a few new episodes for the show we made`_
    - `Add the episodes to a playlist`_
    - `Control the media player`_

Setup the client
----------------

To setup the client you will need to install Slumber, then create an API object::

    >>> import slumber
    >>> api = slumber.API("http://localhost:8000/api/v1/")

List all TV shows, drill down a bit deeper for a particular show
-----------------------------------------------------------------

To list all TV shows we will call this line of code::

    >>> shows = api.show.get()
    >>> show
    {u'meta': {u'previous': None, u'total_count': 0, u'offset': 0, u'limit': 20, u'next': None}, u'objects': []}

Now let's grab a detail version of the first show object::

    >>> show = api.show(1).get()
    >>> THIS IS THE SHOW

How about seeing all episodes this show has::

    >>> episodes = api.show(1).episodes.get()
    >>> episodes
    >>> THIS IS THE EPISODES

Create a new TV show
--------------------

Now let's POST a new show object - it's easy! ::

    >>> new_show = api.show.post({ "name": "The Office UK"})
    >>> NEW SHOW ECHOED

Create a few new episodes for the show we made
----------------------------------------------

All we need to do is POST a few new episodes, specifying the show as the one we just created ::

    >>> ep1 = api.episode.post({ "name": "Episode 01", "show": new_show })
    >>> ep2 = api.episode.post({ "name": "Episode 02", "show": new_show })
    >>> ep3 = api.episode.post({ "name": "Episode 03", "show": new_show })

Add the episodes to a playlist
------------------------------

Now let's add these new episodes to a new playlist::

    >>> playlist = api.playlist.post({ "name", "My favourite office episodes" })
    >>> playlist = api.playlist.patch({ "content",  [
                                                    { "resource_uri": ep1 },
                                                    { "resource_uri": ep2 },
                                                    { "resource_uri": ep3 },
                                                    ]}

Control the media player
------------------------

As there is only one 'player', it is represented by one resource at /api/v1/player/. To command you need to pass
arguments via the ?action parameter ::

    >>> player = api.player.get(action='play')
    >>> player['status']
    >>> 'playing'
    >>> player = api.player.get(action='pause')
    >>> player['status']
    >>> 'paused'

Available actions are: play, pause, stop, next, back.