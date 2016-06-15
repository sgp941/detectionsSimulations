#!/usr/bin/python

import os
import time
from subprocess import call
import Image
import ImageDraw
# import ImageOps
import numpy as np
import ImageChops
import glob
import sys

coord = [(143, 566), (474, 290), (707, 180), (940, 120), (1340, 50), (1806, 16), (2151, 20), (2583, 82), 
		 (2780, 142), (3078, 254), (3440, 454), (3232, 627), (2900, 806), (2468, 981), (1966, 1060), 
		 (1588, 1066), (1238, 1006), (692, 848), (338, 700)]

folder = str(sys.argv[1])
maxW = 3840.0
maxH = 1080.0




pngFiles = glob.glob(folder + "/*.png")

totalFiles = len(pngFiles)


for (i, filename) in enumerate(pngFiles):

	print "Cleaned " + str(i) + " Of " + str(totalFiles) + " Images"

	image = Image.open(filename)

	w = image.size[0]
	h = image.size[1]


	scaledCoord  =[(round(x*(w/maxW)), round(y*(h/maxH))) for (x, y) in coord]

	im = Image.open(filename)

	overlay = Image.new('RGBA', im.size)

	draw = ImageDraw.Draw(overlay)

	draw.polygon(scaledCoord, fill=(255,255,255), outline=(0, 0, 0))

	inverted_overlay = ImageChops.invert(overlay)


	im.paste("black", (0,0), mask=inverted_overlay)

	im.save(filename)

