API Documentation
=================

A full guide to all resources provided by the Media Centre API.

The API is also self-documenting, ``GET /api/v1/`` is a great starting point.

Appending ``/schema/`` to any Resource will get a description of that Resource.

The API root is at ``http://api.tim-garner.co.uk/``

Film
----

.. http:method:: GET /api/v1/film/?name

   :optparam name: Search for Film containing name

   Retrieve list of Films


.. http:method:: GET /api/v1/film/{id}/

   :arg id: An id

   Retrieve Film matching given id.


.. http:method:: POST /api/v1/film/

   :response 202: A Film was created successfully.

   Create a Film


.. http:method:: POST /api/v1/film/{id}/

   :arg id: An id

   :response 202: The Film was updated successfully.

   Update Film matching given id

.. note::

   PATCH and PUT are both available and work in a similar fashion to POST


.. http:method:: DELETE /api/v1/film/

   :response 202: The Films were deleted successfully.

   Delete *all* Films


.. http:method:: DELETE /api/v1/film/{id}/

   :arg id: An id

   :response 202: The Film was deleted successfully.

   Delete film



FilmSeries
----------

.. http:method:: GET /api/v1/filmseries/?name

   :optparam name: Search for Filmseries containing name

       Retrieve list of Filmseriess


.. http:method:: GET /api/v1/filmseries/{id}/

   :arg id: An id

       Retrieve Filmseries matching given id.


.. http:method:: POST /api/v1/filmseries/

   :response 202: A Filmseries was created successfully.

       Create a Filmseries


.. http:method:: POST /api/v1/filmseries/{id}/

   :arg id: An id

       :response 202: The Filmseries was updated successfully.

       Update Filmseries matching given id

.. note::

   PATCH and PUT are both available and work in a similar fashion to POST


.. http:method:: DELETE /api/v1/filmseries/

   :response 202: The Filmseriess were deleted successfully.

   Delete *all* Filmseriess


.. http:method:: DELETE /api/v1/filmseries/{id}/

   :arg id: An id

   :response 202: The Filmseries was deleted successfully.

   Delete filmseries
   
   

Episode
-------


.. http:method:: GET /api/v1/episode/?name

   :optparam name: Search for Episode containing name

       Retrieve list of Episodes


.. http:method:: GET /api/v1/episode/{id}/

   :arg id: An id

       Retrieve Episode matching given id.


.. http:method:: POST /api/v1/episode/

   :response 202: A Episode was created successfully.

       Create a Episode


.. http:method:: POST /api/v1/episode/{id}/

   :arg id: An id

       :response 202: The Episode was updated successfully.

       Update Episode matching given id

.. note::

   PATCH and PUT are both available and work in a similar fashion to POST


.. http:method:: DELETE /api/v1/episode/

   :response 202: The Episodes were deleted successfully.

   Delete *all* Episodes


.. http:method:: DELETE /api/v1/episode/{id}/

   :arg id: An id

   :response 202: The Episode was deleted successfully.

   Delete episode
   

Show
----


.. http:method:: GET /api/v1/show/?name

   :optparam name: Search for Show containing name

       Retrieve list of Shows


.. http:method:: GET /api/v1/show/{id}/

   :arg id: An id

       Retrieve Show matching given id.


.. http:method:: POST /api/v1/show/

   :response 202: A Show was created successfully.

       Create a Show


.. http:method:: POST /api/v1/show/{id}/

   :arg id: An id

       :response 202: The Show was updated successfully.

       Update Show matching given id

.. note::

   PATCH and PUT are both available and work in a similar fashion to POST


.. http:method:: DELETE /api/v1/show/

   :response 202: The Shows were deleted successfully.

   Delete *all* Shows


.. http:method:: DELETE /api/v1/show/{id}/

   :arg id: An id

   :response 202: The Show was deleted successfully.

   Delete show
   
   

Content
-------

.. warning::

   Content is the parent of Film and Episode Resources. You cannot directly create, update or delete a Content Resource.

.. http:method:: GET /api/v1/content/?name

   :optparam name: Search for Content containing name

       Retrieve list of Contents


.. http:method:: GET /api/v1/content/{id}/

   :arg id: An id

       Retrieve Content matching given id.

   
   

Playlist
--------


.. http:method:: GET /api/v1/playlist/?name

   :optparam name: Search for Playlist containing name

       Retrieve list of Playlists


.. http:method:: GET /api/v1/playlist/{id}/

   :arg id: An id

       Retrieve Playlist matching given id.


.. http:method:: POST /api/v1/playlist/

   :response 202: A Playlist was created successfully.

       Create a Playlist


.. http:method:: POST /api/v1/playlist/{id}/

   :arg id: An id

       :response 202: The Playlist was updated successfully.

       Update Playlist matching given id

.. note::

   PATCH and PUT are both available and work in a similar fashion to POST


.. http:method:: DELETE /api/v1/playlist/

   :response 202: The Playlists were deleted successfully.

   Delete *all* Playlists


.. http:method:: DELETE /api/v1/playlist/{id}/

   :arg id: An id

   :response 202: The Playlist was deleted successfully.

   Delete playlist
   

Player
------

.. note::

    There is only *one* Player, you cannot create, update or delete it.


.. http:method:: GET /api/v1/player/?action

   :optparam action: Command player to perform action.
                     Actions available: play, pause, stop, back, next.

   Retrieve Player





