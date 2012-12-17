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


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        def callback(data):
            pass
        def errback(failure):
            self.fail()
        self.callback = callback
        self.errback = errback

        self.api = txlastfmapi.LastFmApi(SAMPLE_API_KEY)


class TestApiAlbumMethods(ApiTestCase):

    def setUp(self):
        super(TestApiAlbumMethods, self).setUp()
        self.kwargs = {
            'artist': 'cher',
            'album': 'believe',
            'country': 'united states',
        }

    def test_api_album_getBuylinks(self):
        return self.api.album_getBuylinks(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_album_getInfo(self):
        return self.api.album_getInfo(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_album_getTags(self):
        return self.api.album_getTags(user='RJ', **self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_album_getTopTags(self):
        return self.api.album_getTopTags(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_album_search(self):
        return self.api.album_search(**self.kwargs).addCallbacks(
            self.callback, self.errback)


class TestApiArtistMethods(ApiTestCase):

    def setUp(self):
        super(TestApiArtistMethods, self).setUp()
        self.kwargs = {
            'artist': 'cher',
        }

    def test_api_artist_getCorrection(self):
        return self.api.artist_getCorrection(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getEvents(self):
        return self.api.artist_getEvents(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getInfo(self):
        return self.api.artist_getInfo(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getPastEvents(self):
        return self.api.artist_getPastEvents(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getPodcast(self):
        return self.api.artist_getPodcast(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getShouts(self):
        return self.api.artist_getShouts(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getSimilar(self):
        return self.api.artist_getSimilar(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getTags(self):
        return self.api.artist_getTags(user='RJ', **self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getTopAlbums(self):
        return self.api.artist_getTopAlbums(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getTopFans(self):
        return self.api.artist_getTopFans(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getTopTags(self):
        return self.api.artist_getTopTags(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_getTopTracks(self):
        return self.api.artist_getTopTracks(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_artist_search(self):
        return self.api.artist_search(**self.kwargs).addCallbacks(
            self.callback, self.errback)


class TestApiTrackMethods(ApiTestCase):
    '''Tests to make sure all unauthenticated track methods work.'''

    def setUp(self):
        super(TestApiTrackMethods, self).setUp()
        self.kwargs = {
            'artist': 'radiohead',
            'track': 'creep',
            'country': 'united states',
        }

    def test_api_track_getBuylinks(self):
        return self.api.track_getBuylinks(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_getCorrection(self):
        return self.api.track_getCorrection(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_getFingerprintMetadata(self):
        return self.api.track_getFingerprintMetadata(
            fingerprintid='1234', **self.kwargs).addCallbacks(
                self.callback, self.errback)

    def test_api_track_getInfo(self):
        return self.api.track_getInfo(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_getShouts(self):
        return self.api.track_getShouts(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_getSimilar(self):
        return self.api.track_getSimilar(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_getTags(self):
        return self.api.track_getTags(user='RJ', **self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_getTopFans(self):
        return self.api.track_getTopFans(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_getTopTags(self):
        return self.api.track_getTopTags(**self.kwargs).addCallbacks(
            self.callback, self.errback)

    def test_api_track_search(self):
        return self.api.track_search(**self.kwargs).addCallbacks(
            self.callback, self.errback)

