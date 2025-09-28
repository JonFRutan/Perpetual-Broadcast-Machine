from spotdl import Spotdl
from spotdl.download import Downloader
from spotdl.types.playlist import Playlist
from spotdl.types.song import Song
import dotenv

playlist = input("Profide a spotifyurl: ")
spotdl = Spotdl(client_id="f8a606e5583643beaa27ce62c48e3fc1", client_secret="f6f4c8f73f0649939286cf417c811607")
playlist = Playlist.from_url(playlist)

for song in playlist.songs:
    print(f"{song.name} - {song.url}")