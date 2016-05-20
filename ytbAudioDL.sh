#!/bin/bash

youtube-dl -x --audio-quality 0 --audio-format wav --ignore-errors --exec 'sh upload.sh' $@
