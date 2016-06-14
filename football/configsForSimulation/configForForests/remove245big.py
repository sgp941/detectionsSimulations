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
"train_pos_1_1",
"train_pos_2_1",
"train_pos_2_2",
"train_pos_3_1",
"train_pos_3_2",
"train_pos_3_3",
"train_pos_4_1",
"train_pos_4_2",
"train_pos_4_3",
"train_pos_4_4"
]



for folder in filenames:

	foldercontents = os.listdir(folder)

	getID = [(int(re.findall(r'\d+', x)[0]), x) for x in foldercontents]

	for (i, iName) in getID:
		if (i > 2054):
			os.remove(folder + "/" + iName)


	# # print

	# # print [int(s) for s in filename.split() if s.isdigit()]

	# # content = []
	# with open(filename) as f:
	# 	content = []
	# 	content = f.readlines()
	# 	content.pop(0)
	# 	content = [line for line in content if int(line[3:7]) % 13 != 0]


	# content = [str(size) + " 1\n"] + content
	# content = content[0:size+1]
	# # print content[0:size]
	# print filename


	# saveFileArray(filename, content)
	# print content
	    # saveFileArray(filename, content)
	    





#DO THIS SHIT<
#ITERATE LINE BY LINE, ADDING OT NEW CONTENT
#PUSH TO FUCKER TO NEW FILE






