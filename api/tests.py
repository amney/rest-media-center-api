"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from tastypie.test import ResourceTestCase
from api.api_models import FilmResource
from api.models import Film, FilmSeries


class FilmResourceTest(ResourceTestCase):
    # Use ``fixtures`` & ``urls`` as normal. See Django's ``TestCase``
    # documentation for the gory details.
    fixtures = ['test_entries.json']

    def setUp(self):
        super(FilmResourceTest, self).setUp()

        # Create a user.
        self.name = 'Die Hard'
        self.film_series = FilmSeries.objects.create(name='Die Hard Trilogy')
        self.film = Film.objects.create(name=self.name, film_series=self.film_series)

        self.detail_url = '/api/v1/film/{0}/'.format(self.film.pk)

        # The data we'll send on POST requests. Again, because we'll use it
        # frequently (enough).
        self.post_data = {
            'user': '/api/v1/user/{0}/'.format(self.film.pk),
            'title': 'Second Post!',
            'slug': 'second-post',
            'created': '2012-05-01T22:05:12'
        }

    ''' def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_get_list_unauthorzied(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/entries/', format='json'))
    '''

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/film/', format='json')
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)

        # Here, we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            'film_series': '/api/v1/filmseries/{0}/'.format(self.film_series.pk),
            'id': self.film.pk,
            'name': self.film.name,
            'resource_uri': '/api/v1/film/{0}/'.format(self.film.pk)
        })

    '''
    def test_get_list_xml(self):
        self.assertValidXMLResponse(self.api_client.get('/api/v1/entries/', format='xml', authentication=self.get_credentials()))

    def test_get_detail_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get(self.detail_url, format='json'))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp), ['created', 'slug', 'title', 'user'])
        self.assertEqual(self.deserialize(resp)['name'], 'First post')

    def test_get_detail_xml(self):
        self.assertValidXMLResponse(self.api_client.get(self.detail_url, format='xml', authentication=self.get_credentials()))

    def test_post_list_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.post('/api/v1/entries/', format='json', data=self.post_data))

    def test_post_list(self):
        # Check how many are there first.
        self.assertEqual(Entry.objects.count(), 5)
        self.assertHttpCreated(self.api_client.post('/api/v1/entries/', format='json', data=self.post_data, authentication=self.get_credentials()))
        # Verify a new one has been added.
        self.assertEqual(Entry.objects.count(), 6)

    def test_put_detail_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.put(self.detail_url, format='json', data={}))

    def test_put_detail(self):
        # Grab the current data & modify it slightly.
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
        new_data = original_data.copy()
        new_data['title'] = 'Updated: First Post'
        new_data['created'] = '2012-05-01T20:06:12'

        self.assertEqual(Entry.objects.count(), 5)
        self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
        # Make sure the count hasn't changed & we did an update.
        self.assertEqual(Entry.objects.count(), 5)
        # Check for updated data.
        self.assertEqual(Entry.objects.get(pk=25).title, 'Updated: First Post')
        self.assertEqual(Entry.objects.get(pk=25).slug, 'first-post')
        self.assertEqual(Entry.objects.get(pk=25).created, datetime.datetime(2012, 3, 1, 13, 6, 12))

    def test_delete_detail_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.delete(self.detail_url, format='json'))

    def test_delete_detail(self):
        self.assertEqual(Entry.objects.count(), 5)
        self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
        self.assertEqual(Entry.objects.count(), 4)'''