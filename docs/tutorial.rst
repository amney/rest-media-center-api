API Introduction
=================================

The purpose of this guide is to help you get started interacting with the API.

We will go through:
    - Retrieving a list of all films
    - Getting some more detail about a single film
    - Getting a related resource
    - Creating a new film
    - Editing some data about a film
    - Deleting a film

For a detailed look at the structure of the API please see the :doc:`api`.

GET'ing some data out of the system
-----------------------------------

As this is a RESTful service you can modify resources using the common HTTP verbs GET, POST, PUT, PATCH, DELETE.

Object lists can be retrieved by querying the parent resource object. Further detail for individual objects is then
acquired by appending the id to the list resource.

Some detail resources will even provide nested lists, if appropriate.

To GET a list of Films::

    GET /api/v1/film/

.. note::

   You can search for film names by appending the ?name parameter and providing a search string

To GET a detailed view of one film::

    GET /api/v1/film/{id}/

Resources can point to related objects. A film will have a Film Series resource_uri if it belongs to one.
You can retrieve this by::

    GET /api/v1/filmseries/{id}/

.. note::

    Append /films/ to the end of a Film Series detail and it will list all Films in that Series.

POST'ing some data into the system
----------------------------------

To create a new film:

..  code-block:: js

    POST /api/v1/film/

    data: {
            "name": "Lord of the Rings"
          }

To edit a film:

..  code-block:: js

    PATCH /api/v1/film/{id}/

    data: {
            "name": "Lord of the Rings: The Fellowship of the Ring"
          }


DELETE'ing some data from the system
------------------------------------

The DELETE HTTP verb is used::

    DELETE /api/v1/film/{id}/

.. warning::

   You can perform a DELETE against a list, be careful: this will delete *all* objects of that Resource type.


Conclusion
----------

For this example we have used the Film resource, however the principles can be applied across all Resources provided
by the system.

The :doc:`api` has a list of all Resources available.