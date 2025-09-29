#jfr

import dotenv
from src.spdl import Spdl
import src.meta as meta

class PMM:
    def __init__(self):
        self.spdl = Spdl()

    def repl(self):
        pass

def testbed(pmm):
    #Testing grab_songs_from_playlist_url
    playlist_url = "https://open.spotify.com/playlist/6n9Bj1MyUq3Ze1o6OaCd56"
    songs_test = pmm.spdl.grab_songs_from_playlist_url(playlist_url)
    is_correct_count = "PASS" if len(songs_test) == 15 else "FAIL"
    print(f"grab_songs_from_playlist_url result: {is_correct_count}")
    downloads_test = pmm.spdl.download_songs_from_playlist(songs_test, "test_playlist")
    print(downloads_test)


if __name__ == "__main__":
    pmm = PMM()
    testbed(pmm)
