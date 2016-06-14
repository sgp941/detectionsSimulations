#!/usr/bin/python
import string
import os
import re

def saveFile(filename, data):
	# Saving new tokenised file
	dirname = filename
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	fh = open(dirname + "/" + "config.txt", 'w+')
	fh.write(str(data))

def saveFileArray(filename, arrayData):

	os.remove(filename)
	print "SAVING FILE"
	with open(filename, 'w+') as myfile:
		for item in arrayData:
  			myfile.write("%s" % item)

def readFileContents(filename):
	# Opening Base file, and getting the base config
	with open(filename, 'r') as myfile:
	    data = myfile.read()
	return data

def buildCoOrdMap():
	filename = "totalFileCoords.txt"
	contents = []
	map = {}
	with open(filename, 'r') as f:
		contents = f.readlines()
		contents.pop(0)

		for c in contents:
			splitVal = c.split(".png ")
			print splitVal
			key = splitVal[0] + ".png"
			val = splitVal[1]
			map[key] = val

	return map



filenames = [
"train_pos_1_1.txt",
"train_pos_2_1.txt",
"train_pos_2_2.txt",
"train_pos_3_1.txt",
"train_pos_3_2.txt",
"train_pos_3_3.txt",
"train_pos_4_1.txt",
"train_pos_4_2.txt",
"train_pos_4_3.txt",
"train_pos_4_4.txt"
]


filenameMap = buildCoOrdMap()

for filename in filenames:
	folder = filename[:-4]

	picsRequired = os.listdir(folder)[0:100]
	

	# print picsRequired)

	newFileContents = [x + " " + filenameMap[x] for x in picsRequired]

	newFileContents = ["100 1\n"] + newFileContents

	saveFileArray(filename, newFileContents)

	# print newFileContents




#DO THIS SHIT<
#ITERATE LINE BY LINE, ADDING OT NEW CONTENT
#PUSH TO FUCKER TO NEW FILE






