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
    >>> print shows
    {u'meta': {u'previous': None, u'total_count': 2, u'offset': 0, u'limit': 20, u'next': None}, u'objects': [{u'episodes': [u'/api/v1/episode/3/', u'/api/v1/episode/4/'], u'resource_uri': u'/api/v1/show/1/', u'actors': [], u'id': 1, u'name': u'Friends'}, {u'episodes': [u'/api/v1/episode/1/', u'/api/v1/episode/2/'], u'resource_uri': u'/api/v1/show/2/', u'actors': [], u'id': 2, u'name': u'Peep Show'}]}

Now let's grab a detail version of the first show object::

    >>> show = api.show(1).get()
    >>> print show
    >>> {u'episodes': [u'/api/v1/episode/3/', u'/api/v1/episode/4/'], u'resource_uri': u'/api/v1/show/1/', u'actors': [], u'id': 1, u'name': u'Friends'}

How about seeing all episodes this show has::

    >>> episodes = api.show(1).episodes.get()
    >>> episodes
    >>> print episodes
    >>> {u'meta': {u'previous': None, u'total_count': 4, u'offset': 0, u'limit': 20, u'next': None}, u'objects': [{u'plot': u"Rachel leaves her fiance, Barry, at the altar and decides to move in with her old friend Monica after meeting the gang in the coffee place 'Central Perk.' Everyone watches Spanish soap operas at Monica's place. Monica, meanwhile, sleeps with Paul the 'Wine Guy' from her work, who turns out to be less than sincere and lies to get her into bed. Chandler and Joey try to get Ross back into dating who is reeling from his divorce from Carol as he found out she is a lesbian. Ross reveals his high school crush on Rachel and mentions asking her out. Rachel discovers independence isn't as easy as she thought and gets a job at the coffee house as a waitress. ", u'name': u'The Pilot', u'show': u'/api/v1/show/1/', u'file_type': u'mp4', u'season': 1, u'length': u'30:00', u'frame_rate': 60, u'episode_number': 1, u'quality': u'TV', u'id': 1, u'resource_uri': u'/api/v1/episode/1/'}, {u'plot': u"Carol, Ross' lesbian ex-wife, tells him at work that she is pregnant with his child and when he attends the sonogram, is stunned to learn that she wants to give the baby her and her lesbian lover's last names. Monica nearly has a breakdown from stressing when her and Ross' parents come for dinner. Ross and Rachel console each other, as she as to return her engagement ring to Barry and finds out that he and her maid of honor Mindy, went on her honeymoon.", u'name': u'The One with the Sonogram and the End', u'show': u'/api/v1/show/1/', u'file_type': u'mp4', u'season': 1, u'length': u'29:39', u'frame_rate': 60, u'episode_number': 2, u'quality': u'TV', u'id': 2, u'resource_uri': u'/api/v1/episode/2/'}, {u'plot': u"Monica becomes irritated when everyone likes her new boyfriend Alan, more than she does. Chandler starts smoking again and when the group complains he diverts their attention to their own faults. Phoebe gets money put into her account that isn't hers and when she complains she gets more so she gives it to her homeless friend who buys her a can of soda, only to find a thumb in the can of soda. Phoebe uses the money from the soda company to pay Chandler to quit smoking. ", u'name': u'The One with the Thumb', u'show': u'/api/v1/show/1/', u'file_type': u'mp4', u'season': 1, u'length': u'29:59', u'frame_rate': 60, u'episode_number': 3, u'quality': u'TV', u'id': 3, u'resource_uri': u'/api/v1/episode/3/'}, {u'plot': u"Ross, upset about it being the anniversary of his first time sleeping with Carol, goes to a hockey game with Chandler and Joey and gets a puck hit in his face so they end up at the hospital. There, Ross reveals Carol is the only woman he's ever slept with. Rachel gets her first pay check but is angry that most of her money went to FICA, and also gets a visit from her old friends, which depresses her further about her new life. To cheer her up, Monica and Phoebe have a slumber party which isn't very fun due to Rachel's depressed state, until the girls spy on the sexy politician across the street (George Stephanopoulos) whose pizza was delivered to them by mistake. ", u'name': u'The One with George Stephanopoulos', u'show': u'/api/v1/show/1/', u'file_type': u'mp4', u'season': 1, u'length': u'31:30', u'frame_rate': 60, u'episode_number': 4, u'quality': u'TV', u'id': 4, u'resource_uri': u'/api/v1/episode/4/'}]}

Create a new TV show
--------------------

Now let's POST a new show object - it's easy! ::

    >>> new_show = api.show.post({ "name": "The Office UK"})
    >>> print new_show
    >>> {u'episodes': [], u'resource_uri': u'/api/v1/show/10/', u'actors': [], u'id': 10, u'name': u'The Office UK'}

Create a few new episodes for the show we made
----------------------------------------------

All we need to do is POST a few new episodes, specifying the show as the one we just created ::

    >>> ep1 = api.episode.post({"episode_number": "1", "season_number": "1", "length": "30:00", "name": "Downsize", "plot": "plot1", "show": new_show})
    >>> ep2 = api.episode.post({"episode_number": "2", "season_number": "1", "length": "30:00", "name": "Work Experience", "plot": "plot2", "show": new_show})
    >>> ep3 = api.episode.post({"episode_number": "3", "season_number": "1", "length": "30:00", "name": "The Quiz", "plot": "plot3", "show": new_show})

Add the episodes to a playlist
------------------------------

Now let's add these new episodes to a new playlist. We'll do this in two steps to demonstrate the ``PATCH`` verb.

First we will create the playlist::

    >>> playlist = api.playlist.post({ "name", "My favourite office episodes" })

Now patch the ``content`` of the playlist we just created to point to the three new episodes::

    >>> playlist = api.playlist(playlist['id']).patch({"content": [{ "resource_uri": ep1 }, { "resource_uri": ep2 }, { "resource_uri": ep3 }]})
    >>> print playlist
    >>> {u'auto_create_time': u'2013-02-17T20:26:12.547126', u'name': u'My favourite office episodes', u'auto_modify_time': u'2013-02-17T20:29:06.236324', u'content': [u'/api/v1/content/21/', u'/api/v1/content/22/', u'/api/v1/content/23/'], u'id': 4, u'resource_uri': u'/api/v1/playlist/4/'}

Control the media player
------------------------

As there is only one 'player', it is represented by one resource at /api/v1/player/. To command you need to pass
arguments via the ?action parameter ::

    >>> player = api.player.get(action='play')
    >>> print player['status']
    >>> 'playing'
    >>> player = api.player.get(action='pause')
    >>> print player['status']
    >>> 'paused'

Available actions are: play, pause, stop, next, back.