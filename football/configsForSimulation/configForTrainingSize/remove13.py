#!/usr/bin/python
import string
import os

def saveFile(filename, data):
	# Saving new tokenised file
	dirname = filename
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	fh = open(dirname + "/" + "config.txt", 'w+')
	fh.write(str(data))


def readFileContents(filename):
	# Opening Base file, and getting the base config
	with open(filename, 'r') as myfile:
	    data = myfile.read()
	return data

filenames = [
"train_pos_12.txt", 
# "train_pos_24.txt", 
# "train_pos_48.txt"
# "train_pos_96.txt", 
# "train_pos_192.txt", 
# "train_pos_384.txt", 
# "train_pos_1536.txt", 
# "train_pos_768.txt", 
]



for filename in filenames:
	with open(filename) as f:
	    content = f.readlines()
	 	print content







