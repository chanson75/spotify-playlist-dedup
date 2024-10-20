import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
client_id = 'e91a6987d2744aa3b7b6084f89f905ae'
client_secret = '6d54ba82376c4386addc034e25a9e342'
redirect_uri = 'https://spotify.com'
scope = 'playlist-modify-public playlist-modify-private playlist-read-private'

print("hello")
# Authenticate and get the access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

print("hello")
# Your playlist ID
playlist_id = '5kcM6SPoZzQGhX1sKS2ell'

# Get all tracks in the playlist
results = sp.playlist_tracks(playlist_id)
tracks = results['items']

# Fetch all tracks if the playlist is large
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# Identify duplicates
track_ids = [track['track']['id'] for track in tracks]
duplicates = [track for track in tracks if track_ids.count(track['track']['id']) > 1]

# Remove duplicates
for duplicate in duplicates:
    sp.playlist_remove_all_occurrences_of_items(playlist_id, [duplicate['track']['id']])

print("Duplicates removed.")
