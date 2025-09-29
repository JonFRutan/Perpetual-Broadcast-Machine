#jfr
#WIP

# This class will update and modify the radio.liq file that runs the audio streams
# Features it will need:
# - Adding stations (station_name, stream_ref)
#   - This should create a playlist using the stream_ref name
# - Deleting stations (station_name)
# - Configuring station settings like crossfade
#
# Design ideas:
# - Stations in radio.liq should be delimited for file parsing: #####<STREAM_REF>#####
