#jfr

import sys
import src.meta as meta

from pathlib import Path
from src.spdl import Spdl

class PMM:
    def __init__(self):
        self.spdl = Spdl()

    def repl(self):
        pass

def testbed(pmm):
    #Testing grab_songs_from_playlist_url
    playlist_url = "https://open.spotify.com/playlist/39K8zRiSK1IUziBTMsQCaq"
    songs_test = pmm.spdl.grab_songs_from_playlist_url(playlist_url)
    is_correct_count = "PASS" if len(songs_test) == 5 else "FAIL"
    print(f"grab_songs_from_playlist_url result: {is_correct_count}")
    downloads_test = pmm.spdl.download_songs_from_playlist(songs_test, "test_playlist")
    downloads_occurred = "PASS" if len(downloads_test) > 5 else "FAIL"
    print(f"download_songs_from_playlist result: {downloads_occurred}")
    m3u_path = Path(f"{meta.LOCAL_PLAYLIST_STORAGE}/test_playlist.m3u8")
    m3u_file_exists = "PASS" if Path.exists(m3u_path) else "FAIL"
    print(f"m3u file generation result: {m3u_file_exists}")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = sys.argv
        #print(args)
        if args[1] == "--test":
            pmm = PMM()
            testbed(pmm)
            exit()
