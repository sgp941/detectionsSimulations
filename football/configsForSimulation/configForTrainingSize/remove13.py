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

filenames = [
"train_pos_12.txt", 
"train_pos_24.txt", 
"train_pos_48.txt",
"train_pos_96.txt", 
"train_pos_192.txt", 
"train_pos_384.txt", 
"train_pos_1536.txt", 
"train_pos_768.txt", 
]



for filename in filenames:

	size = int(re.findall(r'\d+', filename)[0])
	# print

	# print [int(s) for s in filename.split() if s.isdigit()]

	# content = []
	with open(filename) as f:
		content = []
		content = f.readlines()
		content.pop(0)
		content = [line for line in content if int(line[3:7]) % 13 != 0]


	content = [str(size) + " 1\n"] + content
	content = content[0:size+1]
	# print content[0:size]
	print filename


	saveFileArray(filename, content)
	# print content
	    # saveFileArray(filename, content)
	    





#DO THIS SHIT<
#ITERATE LINE BY LINE, ADDING OT NEW CONTENT
#PUSH TO FUCKER TO NEW FILE






