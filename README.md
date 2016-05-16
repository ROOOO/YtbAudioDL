# DISCRIPTION
 Download Youtube videos and convert them to Audio Format On your own Server. Then, download them easily.

## Requirements
- youtube-dl
- Python 2.x
- ffmepg
- wget
- http-server (Python's build-in HTTPServer is unstable)
 `npm install http-server -g`

## Usage
 - On Server Side
    sh ytbAudioDL.sh [OPTIONS] URL [URL ...]
    python getPlayListURLs PlayListURL
 - On Local Side
    python ytbDL.py [OPTIONS] Protocol://IP

### Notes
 - URL can be a playlist.

## OPTIONS
 - Server
  `-x --audio-quality 0 --audio-format 'aac'` as default args. You can also add youtube-dl build-in OPTIONS if you want.
  `-a toBeDownload`      Add a list of urls after running the getPlayListURLs.py.
 - Local
  -p         Server port(default 23333)
  -o         The directory prefix. (The same as `wget -P`)

## DISCRIPTION
 0. [OPTIONAL] Run `python getPlayListURLs.py PlayListURL` first.
 1. Run `ytbAudioDL.sh` on server.
 2. Run `ytbDL.py` on local for downloading audio files you downloaded on server.

## TODO
 1. Delete audio files which you'd downloaded from your own server.
 2. PlayList

## Release Log
 - v0.2.0
  1. Get all playlists and choose what you are going to download.
 - v0.1.1
  1. Add local file existing detected test. It is no need for downloading the same audio file again.
 - v0.1.0
  1. Working!
