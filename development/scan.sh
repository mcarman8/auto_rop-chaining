#!/bin/bash
FILES=./functions/*
mkdir ./rets
for f in $FILES
do
	if cat $f | grep ret
       	then
		mv $f ./rets
	fi
done
