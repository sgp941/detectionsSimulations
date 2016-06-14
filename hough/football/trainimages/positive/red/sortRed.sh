#!/bin/bash



while [ `ls | wc -l` != '3' ]
do
	mv `ls | head -1` ./tgoal
	mv `ls | head -5` ./tplay
done