#!/usr/bin/python

import os
import time
from PIL import Image
import ImageDraw
import numpy as np

filename = "pic.png"

w = 3840
h = 1080
y = [0.509722222222222,0.135185185185185,0.0194444444444444,0.0782407407407407,0.427777777777778,0.993518518518519,1];
x = [0.0317708333333333,0.222786458333333,0.463020833333333,0.682031250000000,0.912239583333333,0.600911458333333,0.338281250000000];

y = [round(z) for z in h*np.array(y)]
x = [round(z) for z in w*np.array(x)]

print x
print y

coord = [(val,y[i]) for (i,val) in enumerate(x)]

print coord

im = Image.open(filename)
im 
# im.show()
bg = Image.new("RGB", im.size, (255,255,255))
Image.alpha_composite(im,bg).show()
# bg.paste(im,mask=bg)
# bg.show()

'''
back = im
poly = Image.new('RGB', [w,h])
pdraw = ImageDraw.Draw(poly)
pdraw.polygon(coord,
	fill=(0,0,0),outline=(255,255,255))
back.paste(poly,mask=poly)
back.show()
'''





'''
back = Image.new('RGBA', (512,512), (255,0,0,0))
poly = Image.new('RGBA', (512,512))
pdraw = ImageDraw.Draw(poly)
pdraw.polygon([(128,128),(384,384),(128,384),(384,128)],
	fill=(255,255,255,127),outline=(255,255,255,255))
back.paste(poly,mask=poly)
back.show()
'''