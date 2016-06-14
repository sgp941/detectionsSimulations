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

samples = [12,24,48,96,192,384,768,1536]

baseFileName = 'config_base.txt'

# Replacing tokens
for i in samples:	
	filename = "trainingSize_"
	data = readFileContents(baseFileName)
	data = data.replace("<x>", "train_pos_" + str(i) + ".txt")
	data = data.replace("<y>", "train_neg_" + str(i) + ".txt")
	filename = filename + str(i)
	saveFile(filename, data)

