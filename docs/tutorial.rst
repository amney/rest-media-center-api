API Introduction
=================================

The purpose of this guide is to help you get started interacting with the API.

We will go through:
    - Authenticating
    - Authorization
    - Retrieving a list of all films
    - Getting some more detail about a single film
    - Getting a related resource
    - Creating a new film
    - Editing some data about a film
    - Deleting a film

For a detailed look at the structure of the API please see the :doc:`api`.

Authentication
--------------

Authentication is a very import of an API - it defines *who* is allowed to interact with the API. For the purposes
of this Coursework I have created an user that can Authenticate with an API Key.

To Authenticate you can do it either via passing URL parameters, or in a header.

Using URL Parameters::

    GET /{resource}/?username=api&api_key=a112cc8d84bfdcc5d04eefd87ac9b3a81d677f44

Using a Header::

     Authorization: ApiKey api:a112cc8d84bfdcc5d04eefd87ac9b3a81d677f44

If using the Postman client the Header field would look as such:

    .. image:: _static/postman.png

Authorization
-------------

Authorization is concerned with *what* the authenticated user is allowed to do. Luckily the api user we authenticated
with above has full permissions to do anything!


GET'ing some data out of the system
-----------------------------------

As this is a RESTful service you can modify resources using the common HTTP verbs GET, POST, PUT, PATCH, DELETE.

Object lists can be retrieved by querying the parent resource object. Further detail for individual objects is then
acquired by appending the id to the list resource.

Some detail resources will even provide nested lists, if appropriate.

To GET a list of Films::

    GET /api/v1/film/

    Returns HTTP 200 OK on Success

.. note::

   You can search for films by name by appending the ?name parameter and providing a search string

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

    data:
    {
        "name": "Lord of The Rings",
        "file_type": "mkv",
        "frame_rate": "24",
        "length": "1:45:00",
        "plot": "An Epic Adventure",
        "quality": "Blu-Ray",
        "release_date": "2001-10-12"
    }

    Returns HTTP 201 Created on Success

To edit a film:

..  code-block:: js

    PATCH /api/v1/film/{id}/

    data:
    {
        "name": "Lord of the Rings: The Fellowship of the Ring"
    }

    Returns HTTP 202 Accepted on Success

DELETE'ing some data from the system
------------------------------------

The DELETE HTTP verb is used::

    DELETE /api/v1/film/{id}/

    Returns HTTP 204 No Content on Success
    
.. warning::

   You can perform a DELETE against a list, be careful: this will delete *all* objects of that Resource type.


Conclusion
----------

For this example we have used the Film resource, however the principles can be applied across all Resources provided
by the system.

The :doc:`api` has a list of all Resources available.