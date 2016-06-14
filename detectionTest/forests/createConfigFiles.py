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


numTrees = [1,2,5,10,15,20]
patchSize = [10,16,20]
#patchWidth = [10,16,20]
#patchHeight = [10,16,20]
samplePatches = [10,20,50,100]
#samplePatchesPos = [10,20,50,100]
#samplePatchesNeg = [10,20,50,100]
trainingSize = [13,26,52,104]


baseFileName = 'config_base.txt'
delim = ","

# Replacing tokens
for i in numTrees:
	for j in patchSize:
		for k in samplePatches:
			for l in trainingSize:
				#for m in samplePatchesNeg:
				#	for n in trainingSize:
						data = readFileContents(baseFileName)
						data = data.replace("<numTrees>", str(i))
						data = data.replace("<patchWidth>", str(j))
						data = data.replace("<patchHeight>", str(j))
						data = data.replace("<samplePatchesPos>", str(k))
						data = data.replace("<samplePatchesNeg>", str(k))
						data = data.replace("<trainingSize>", str(l))
						filename = str(i) + delim + str(j) + delim + str(k) + delim + str(l)
						saveFile(filename, data)








	#	i :	 <numTrees>
	#	j :	 <patchWidth>
	#	k :	 <patchHeight>
	#	l :	 <samplePatchesPos>
	#	m :	 <samplePatchesNeg>


