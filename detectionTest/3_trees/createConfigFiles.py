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


samples = [1, 4, 8, 12, 16, 20]

baseFileName = 'config_base.txt'

# Replacing tokens
for i in samples:	
	filename = "numTree_"
	data = readFileContents(baseFileName)
	data = data.replace("<x>", str(i))
	filename = filename + str(i)
	saveFile(filename, data)

