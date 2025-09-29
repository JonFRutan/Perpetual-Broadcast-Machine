#jfr
#WIP
#SpotDL Functions

# This class will handle spotdl functions and integrations
# Features it will need:
# - Downloading songs
# - Grabbings songs from playlist
# - Providing song info

import spotipy, time
import src.meta as meta

from pathlib import Path
from spotdl import Spotdl
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException
from spotdl.utils import spotify, m3u
from spotdl.download.downloader import Downloader
from spotdl.types.playlist import Playlist
from spotdl.types.song import SongList

def set_custom_client(client_id, client_secret):
    auth_manager = SpotifyClientCredentials(client_id, client_secret)
    spotify.spotify_client = spotipy.Spotify(auth_manager=auth_manager)

class Spdl:
    def __init__(self):
        self.client_id = meta.SPOTIPY_CLIENT_ID
        self.client_secret = meta.SPOTIPY_CLIENT_SECRET
        self.spotdl = Spotdl(client_id=self.client_id, client_secret=self.client_secret)
        auth_manager = SpotifyClientCredentials(self.client_id, self.client_secret)
        spotify.spotify_client = spotipy.Spotify(auth_manager=auth_manager)


    #FIXME
    # m3u file generation output is broken.
    def download_songs_from_playlist(self, playlist, playlist_reference):
        #Will download music to the LOCAL_MUSIC_STORAGE variable location in the .env
        #As defined by the settings in __init__
        settings = {
            "simple_tui": True,
            "set_live": False,
            "output": meta.LOCAL_MUSIC_STORAGE+'/{title}'
        }
        playlist_path = Path(f"{meta.LOCAL_PLAYLIST_STORAGE}/{playlist_reference}.m3u8")
        temp_path = Path(f"{playlist_reference}.m3u")
        m3u.create_m3u_file(temp_path, playlist, settings["output"], "m3u8")
        temp_path.rename(playlist_path)
        downloader = Downloader(settings)
        return downloader.download_multiple_songs(playlist)

    def grab_song_titles_from_playlist_url(self, url):
        songs = self.grab_songs_from_playlist(url)
        song_titles = []
        for song in songs:
            song_titles.append(song.name)
        return song_titles
    
    def grab_songs_from_playlist_url(self, url):
        while True:
            try:
                playlist = Playlist.from_url(url, True)
                break
            except SpotifyException as e:
                if e.http_status == 429:
                    retry_after = int(e.headers.get("Retry-After", 5))
                    print(f"Rate limited- sleeping for {retry_after}")
                    time.sleep(retry_after)
                else:
                    raise
        return playlist.songs