#!/bin/bash

if [ $# -gt 0 ]; then
	python -m SimpleHTTPServer $1 &
	echo 'port: '$1
else
	python -m SimpleHTTPServer 23333 &
	echo 'prot: 23333'
fi