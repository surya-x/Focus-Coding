from spotify_local import SpotifyLocal

def test(new_status):
    print(new_status)

s = SpotifyLocal()
s.connect()
s.on_status_change += test
s.listen_for_events()