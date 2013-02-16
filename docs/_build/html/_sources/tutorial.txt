API Introduction
=================================

The purpose of this guide is to help you get started interacting with the API.

We will go through:
    - Retrieving a list of all films
    - Getting some more detail about a single film
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

To GET a list of Films post::

    GET http://tim-garner.co.uk/api/v1/film/

To GET a detailed view of one film::

    GET http://tim-garner.co.uk/api/v1/film/1/

POST'ing some data into the system
----------------------------------

To create a new film::

    POST http://tim-garner.co.uk/api/v1/film/

    data: { "name": "Die Hard" }

To edit a film::

    PATCH http://tim-garner.co.uk/api/v1/film/1

    data: { "name": "Die Hard 2" }


DELETE'ing some data from the system
------------------------------------

The DELETE http verb is used ::

    DELETE http://tim-garner.co.uk/api/v1/film/1/


Conclusion
----------

For this example we have used the Film resource, however the principles can be applied across all Resources provided
by the system.

The API Documentation has a list of all Resources available.