# DISCRIPTION
 Download Youtube videos and convert them to Audio Format On your own Server. Then, download them easily.
## Required
- youtube-dl
- Python 2.x
- ffmepg
- wget

## Usage
 - On Server Side
    sh ytbAudioDL.sh [OPTIONS] URL [URL ...]
 - On Local Side
    python ytbDL.py [OPTIONS] IP

### Notes
 - URL can be a playlist.

## OPTIONS
 - Server
  `-x --audio-quality 0` as default args. You can also add youtube-dl build-in OPTIONS if you want.
 - Local
  -p         Server port(default 23333)

## DISCRIPTION
 1. Run `ytbAudioDL.sh` on server.
 2. Run `ytbDL.py` on local for downloading audio files you downloaded on server.

## TODO
 1. Delete audio files which you'd downloaded from your own server.

