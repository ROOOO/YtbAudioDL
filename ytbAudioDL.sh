#!/bin/bash

youtube-dl -x --audio-quality 0 --audio-format mp3 --ignore-errors --embed-thumbnail --exec "sh `pwd`/upload.sh" $@
