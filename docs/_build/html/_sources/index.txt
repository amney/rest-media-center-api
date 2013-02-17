.. SOFT338 Media Centre API documentation master file, created by
   sphinx-quickstart on Fri Feb 15 16:02:18 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SOFT338 Media Centre API's documentation!
====================================================

.. image:: _static/pc.jpg

The essence of the project is that a Media Centre application (e.g. XBMC, Plex, Windows Media Centre) will provide an
API to interact with the content library.

The idea is that the API will provide a set of RESTful Resources that represent the library of TV Shows, Episodes,
Films, Film Series (e.g. Trilogies), and Playlists that map to video files on the Media Centre hard drive(s).

The API is *not designed to upload any media files* but it is designed to:

**Interact with, and manipulate the metadata associated with stored media, organize into playlists, and control the
playback of media on the Media Center device.**

**The API is available at** ``http://api.tim-garner.co.uk/``


Documentation Contents
^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2
   
   tutorial
   example_client
   api
   implementation




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

