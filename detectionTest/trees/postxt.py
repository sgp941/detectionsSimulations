#!/usr/bin/python

import string
import os

from PIL import Image


def get_num_pixels(filepath)
	width,height = Image.open(open(filepath)).size
	return width,height


