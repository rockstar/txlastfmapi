txLastFmApi
-----------

A twisted interface to lastfmapi, which is a dynamic wrapper for accessing the
Last.fm webservice at http://ws.audioscrobbler.com/2.0/ - It's feature set is
identical to lastfmapi, but uses Twisted's asynchronous api rather than a
normal synchronous API.

Installation is easy.

    pip install txlastfmapi

Here's an example for how to use it.

    import txlastfmapi
    
    api = txlastfmapi.LastFmApi('<your api key here>')
    
    def callback(data):
        print data.keys()
    api.album_getInfo(artist='Cher', album='Believe').addCallback(callback)

For methods on the Last.fm api, simply call that method on the api object,
subsituting '_' where '.' would be.
