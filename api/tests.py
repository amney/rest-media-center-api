"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from tastypie.test import ResourceTestCase
from django.test import TestCase
from api.api_models import FilmResource
from api.models import Film, FilmSeries, Player


class PlayerTest(TestCase):
    fixtures = ['api/fixtures/fixtures.json']

    def setUp(self):
        self.player = Player.objects.get(pk=1)

    def test_play(self):
        self.player.play()
        self.assertEqual(self.player.status, 'playing')

    def test_pause(self):
        self.player.pause()
        self.assertEqual(self.player.status, 'paused')

    def test_stop(self):
        self.player.stop()
        self.assertEqual(self.player.status, 'stopped')


class FilmResourceTest(ResourceTestCase):
    fixtures = ['api/fixtures/fixtures.json']

    def setUp(self):
        super(FilmResourceTest, self).setUp()

        print Film.objects.count()
        # Create a user.
        self.name = 'Lord of The Rings: The Fellowship of The Ring'
        self.film_series = FilmSeries.objects.create(name='Lord of The Rings', description='An epic tale')
        self.film = Film.objects.create(name=self.name, film_series=self.film_series,
                                        length='1:00', plot='test')

        self.detail_url = '/api/v1/film/{0}/'.format(self.film.pk)

        # The data we'll send on POST requests. Again, because we'll use it
        # frequently (enough).
        self.post_data = {
            'user': '/api/v1/user/{0}/'.format(self.film.pk),
            'title': 'Second Post!',
            'slug': 'second-post',
            'created': '2012-05-01T22:05:12'
        }

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/film/', format='json')
        self.assertValidJSONResponse(resp)

        # Make sure we have 8 films
        self.assertEqual(len(self.deserialize(resp)['objects']), 8)

        # Check the newest film matches our film object
        api_film = self.deserialize(resp)['objects'][7]
        self.assertEqual(api_film['name'], self.film.name)
        self.assertEqual(api_film['id'], self.film.id)
        self.assertEqual(api_film['quality'], self.film.quality)
        self.assertEqual(api_film['length'], self.film.length)
        self.assertEqual(api_film['release_date'], '1990-07-19')
        self.assertEqual(api_film['film_series'], '/api/v1/filmseries/{0}/'.format(self.film_series.pk))

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)

        # We use ``assertKeys`` here to just verify the keys, not all the data.
        self.assertKeys(self.deserialize(resp),
                        [u'actors',
                         u'file_type',
                         u'film_series',
                         u'frame_rate',
                         u'id',
                         u'length',
                         u'name',
                         u'plot',
                         u'quality',
                         u'release_date',
                         u'resource_uri']
                        )
        self.assertEqual(self.deserialize(resp)['name'], self.film.name)

