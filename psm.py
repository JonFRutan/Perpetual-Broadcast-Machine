#jfr

from spotdl import Spotdl
from spotdl.download.downloader import Downloader
from spotdl.types.playlist import Playlist
from spotdl.types.song import Song
from dotenv import dotenv_values

class PBM:
    def __init__(self):
        env = dotenv_values(".env")
        self.LOCAL_MUSIC_STORAGE = env["LOCAL_MUSIC_STORAGE"]
        self.BROADCAST_LIST      = env["BROADCAST_LIST"]
        self.CLIENT_ID           = env["CLIENT_ID"]
        self.CLIENT_SECRET       = env["CLIENT_SECRET"]

    def grab_songs_from_playlist(self):
        playlist = input("Profide a spotifyurl: ")
        spotdl = Spotdl(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET)
        playlist = Playlist.from_url(playlist)

        for song in playlist.songs:
            print(f"{song.name} - {song.url}")


if __name__ == "__main__":
    pbm = PBM()
    pbm.grab_songs_from_playlist()