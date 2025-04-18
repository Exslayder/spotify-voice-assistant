from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from config.settings import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

def get_spotify_client(scope="user-read-playback-state,user-modify-playback-state,playlist-read-private"):
    return Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI
    ))

def resume():
    sp = get_spotify_client()
    for device in sp.devices()['devices']:
        if device['is_active']:
            sp.start_playback(device['id'])

def next_track():
    sp = get_spotify_client()
    for device in sp.devices()['devices']:
        if device['is_active']:
            sp.next_track(device['id'])

def previous_track():
    sp = get_spotify_client()
    for device in sp.devices()['devices']:
        if device['is_active']:
            sp.previous_track(device['id'])

def pause_if_playing():
    sp = get_spotify_client()
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        for device in sp.devices()['devices']:
            if device['is_active']:
                sp.pause_playback(device['id'])

def play_track(name, lang='en'):
    sp = get_spotify_client()
    results = sp.search(q=name, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        print(f"Now playing: {track['name']}", lang)
        sp.start_playback(uris=[track['uri']])
    else:
        print("Track not found")

def play_playlist(keyword, playlist_keywords, lang='en'):
    sp = get_spotify_client()
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if keyword.lower() in playlist['name'].lower():
            print(f"Now playing playlist: {playlist['name']}", lang)
            sp.start_playback(context_uri=playlist['uri'])
            sp.shuffle(True)
            return
    print("Playlist not found")