# DISCRIPTION
 Download Youtube audios and upload to Google Drive automatically. Then, download them easily from Google Drive.

## Requirements
- youtube-dl
- Python 2.x
- ffmepg
- [gdrive](https://github.com/prasmussen/gdrive)
 - It might be [PyDrive](https://github.com/googledrive/PyDrive) later. :)
- screen
 - `apt-get install screen` On Ubuntu.

## Usage
  python getPlayListURLs PlayListURL
  sh ytbAudioDL.sh [OPTIONS] URL [URL ...]
   - file `parent` for settting parentID on Google Drive.

### Notes
 - URL can be a playlist.

## OPTIONS
  `-x --audio-quality 0 --audio-format 'aac'` as default args. You can also add youtube-dl build-in OPTIONS if you want.
  `-a toBeDownload`      Add a list of urls after running `getPlayListURLs.py`.
  `-o DIR`              For example: -o "./%(uploader)s/%(title)s-%(id)s.%(ext)s"

## DISCRIPTION
 0. [OPTIONAL] Run `python getPlayListURLs.py PlayListURL` first.
 1. Run `ytbAudioDL.sh` on server.

## TODO

## Release Log
 - v0.3.0
  Using Google Drive for data storage.
 - v0.2.2
  1. Enhance Wget procedure.
  2. Beautify output messages.
 - v0.2.1
  1. fix download bugs.
 - v0.2.0
  1. Get all playlists and choose what you are going to download.
 - v0.1.1
  1. Add local file existing detected test. It is no need for downloading the same audio file again.
 - v0.1.0
  1. Working!
