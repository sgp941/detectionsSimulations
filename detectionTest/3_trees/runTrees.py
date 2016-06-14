#!/usr/bin/python

import os
import time
from subprocess import call

dirs = os.listdir(".")
dirs = [x[0] for x in os.walk(".") if "git" not in x[0]]
dirs.pop(0)
print dirs

configFileName = "config.txt"
timeFile = 'timer.txt'

totalDirs = len(dirs)


for (count, dir) in enumerate(dirs):
	print "=============================================================================="
	print "WE ARE ON FILE " + str(count) + " OF " + str(totalDirs)
 	print "=============================================================================="

 	t0 = time.time()
	os.chdir(dir)
	print call("pwd")
	call(["../../HoughForests", "0", configFileName])
	os.chdir("..")
	t1 = time.time()
	total = t1-t0

	dir = dir[2:-4]
	fo = open("timer.txt", "rw+")
	# Write a line at the end of the file.
	fo.seek(0, 2)
	line = fo.write( dir + "," + str(total) + "\n" )
	fo.close()

#	with open("../timer.txt", "a") as myfile:
#   		myfile.write(str(total) + "\n")

	print "=============================================================================="
	print "TEST " + str(count) + " TRAINING TIME: " + str(total) + " seconds"
 	print "=============================================================================="