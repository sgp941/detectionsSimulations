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


samples = ["1_1", "2_1", "2_2", "3_1", "3_2", "3_3", "4_1", "4_2", "4_3", "4_4"]

baseFileName = 'config_base.txt'

# Replacing tokens
for i in samples:	

	filename = "forest"
	data = readFileContents(baseFileName)
	data = data.replace("<xfolder>", "train_pos_" + i)
	data = data.replace("<x>", "train_pos_" + i + ".txt")
	data = data.replace("<yfolder>", "train_neg_" + i)
	data = data.replace("<y>", "train_neg_" + i + ".txt")
	filename = filename + str(i)
	saveFile(filename, data)

