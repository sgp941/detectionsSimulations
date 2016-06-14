#!/bin/bash

while [ `ls | wc -l` != '4' ]
do
	mv `ls | head -6` ./red
	mv `ls | head -6` ./white
	mv `ls | head -1` ./ref
done