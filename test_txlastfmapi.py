from twisted.trial import unittest
import txlastfmapi


SAMPLE_API_KEY = '1b21ef07e3ef3a12197c1d7b7b41b227'

class TestApi(unittest.TestCase):

    def test_api(self):
        def callback(data):
            self.assertEqual(
                data['album']['mbid'],
                '86b5434d-9479-35e3-98ca-8fbcfcf4e357')
        def errback(failure):
            self.fail()

        api = txlastfmapi.LastFmApi(SAMPLE_API_KEY)
        d = api.album_getinfo(artist='Cher', album='Believe')
        d.addCallbacks(callback, errback)
        return d

    def test_api_invalid(self):
        def callback(data):
            self.fail()
        def errback(failure):
            exc = failure.value
            self.assertEqual(
                exc.message,
                'You must supply either an album & artist name or an album mbid.')

        api = txlastfmapi.LastFmApi(SAMPLE_API_KEY)
        d = api.album_getinfo()
        d.addCallbacks(callback, errback)
        return d

