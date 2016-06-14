#!/usr/bin/python
import string
import os

def saveFile(filename, data):
	# Saving new tokenised file
	dirname = filename + "txt1"
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	fh = open(dirname + "/" + "config.txt", 'w+')
	fh.write(str(data))


def readFileContents(filename):
	# Opening Base file, and getting the base config
	with open(filename, 'r') as myfile:
	    data = myfile.read()
	return data



numForests = 1
numTrees = [1,4,8,12,16,20]
patchSize = 16
#patchWidth = [10,16,20]
#patchHeight = [10,16,20]
samplePatches = 50
#samplePatchesPos = [10,20,50,100]
#samplePatchesNeg = [10,20,50,100]
trainingSize = 102

posImgPath = '/home/sgp/Documents/football/trainimages/positive' + str(numForests)
negImgPath = '/home/sgp/Documents/football/trainimages/negative'
testImgPath = '/home/sgp/Documents/football/png'
posTxtPath = './'
negTxtPath = './'
testTxtPath = './'

posTxtName = 'pos.txt'
negTxtName = 'neg.txt'
baseFileName = 'config_base.txt'
delim = ","



dirs = os.listdir(posImgPath)
dirs = [x[0] for x in os.walk('.') if 'git' not in x[0]]
dirs.pop(0)
print dirs





# Replacing tokens
for i in numTrees:
	data = readFileContents(baseFileName)
	data = data.replace("<numTrees>", str(i))
	data = data.replace("<patchWidth>", str(patchSize))
	data = data.replace("<patchHeight>", str(patchSize))
	data = data.replace("<samplePatchesPos>", str(samplePatches))
	data = data.replace("<samplePatchesNeg>", str(samplePatches))
	data = data.replace("<trainingSize>", str(trainingSize))
	filename = str(numForests) + delim + str(i) + delim + str(patchSize) + delim + str(samplePatches) + delim + str(trainingSize)
	saveFile(filename, data)








	#	i :	 <numTrees>
	#	j :	 <patchWidth>
	#	k :	 <patchHeight>
	#	l :	 <samplePatchesPos>
	#	m :	 <samplePatchesNeg>


