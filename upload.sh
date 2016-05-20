#!/bin/bash
parent=`sed -ne '1p' parent`
gdrive upload --delete -p $parent $@
