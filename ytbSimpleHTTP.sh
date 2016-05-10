#!/bin/bash

if [ $# -gt 0 ]; then
	nohup http-server -p $1 &
	echo 'port: '$1
else
	nohup http-server -p 23333 &
	echo 'prot: 23333'
fi
