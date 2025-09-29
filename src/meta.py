#jfr

import dotenv

#Contains meta information relevant to several classes

dotenv.load_dotenv()
env = dotenv.dotenv_values(".env")

LOCAL_MUSIC_STORAGE    = env["LOCAL_MUSIC_STORAGE"]
BROADCAST_LIST         = env["BROADCAST_LIST"]
SPOTIPY_CLIENT_ID      = env["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET  = env["SPOTIPY_CLIENT_SECRET"]
LOCAL_PLAYLIST_STORAGE = env["LOCAL_PLAYLIST_STORAGE"]