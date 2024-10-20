import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'https://spotify.com'
scope = 'playlist-modify-public playlist-modify-private playlist-read-private'

# Authenticate and get the access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Your playlist ID
playlist_id = 'your_playlist_id'

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
