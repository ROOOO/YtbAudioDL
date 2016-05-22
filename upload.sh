#!/bin/bash
parent=`sed -ne '1p' parent.gd`
gdrive upload --delete -p $parent "$@"
