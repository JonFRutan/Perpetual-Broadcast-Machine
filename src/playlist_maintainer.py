#jfr
#WIP

# This class will maintain the set of playlists m3u files for liquidsoap to read from
# Features it will need:
# - Add songs to playlist
# - Remove songs from playlist
# Future features may include:
# - Live-syncing to hooked up playlists
#   - Each playlist object would have an href to a spotify playlist, it can occasionally compare tracks to update

import json
import src.meta as meta
