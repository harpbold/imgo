#!/usr/bin/env python

import os
from PIL import Image
from sys import argv, exit

recursive = False

def help():
	print "Fixes extension for badly named images."
	print "Usage: extfix path [switches]"
	print "Switches:"
	print " -h, -H, -help: Prints help message"
	print " -r, -R: \tOperate on subdirectories too"
	exit(0)

def extensionFix(dir):
	for filename in os.listdir(dir):
		act = dir + os.path.sep + filename
		if os.path.isdir(act):
			if recursive:
				extensionFix(act)
		else:
			ext = os.path.splitext(act)[-1].lower()
			try:
				img = Image.open(act)
				format = img.format
					
				if format == "JPEG":
					if ext not in ('.jpg', '.jpeg'):
						os.rename(act, os.path.splitext(act)[0] + ".jpg")
				if format == "PNG":
					if ext != '.png':
						os.rename(act, os.path.splitext(act)[0] + ".png")
				if format == "GIF":
					if ext != '.gif':
						os.rename(act, os.path.splitext(act)[0] + ".gif")
			except IOError: # for files which only has an image ext but no image data
				pass
					
if __name__ == "__main__":
	if len(argv) == 1:
		print "You must provide a path!"
		exit(-1)
		
	path = argv[1]
	
	if not os.path.exists(path):
		if path == '-h' or path == '-H' or path == '-help':
			help()
		else:
			print "The " + os.path.abspath(path) + " does not exists!"
			print "Aborting script!"
			exit(-1)
	
	extensionFix(argv[1])