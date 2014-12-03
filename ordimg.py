#!/usr/bin/env python

from PIL import Image
import os
from sys import argv, exit
from collections import defaultdict

recursive = False
mapToFolders = defaultdict(list)

def help():
	print "Moves images to folders by their dimensions"
	print "Usage: ordimg path [switches]"
	print "Switches:"
	print " -h, -H, -help: Prints help message"
	print " -r, -R: \tOperates on subdirectories too"
	exit(0)

def sortImgToMap(dir):
	for filename in os.listdir(dir):
		act = dir + os.path.sep + filename
		if os.path.isdir(act):
			if recursive:
				sortImgToMap(act)
		else:
			try:
				img = Image.open(act)
				mapToFolders[img.size].append(os.path.abspath(act))
			except IOError:
				pass
				
def sortImgToDirs():
	for k in mapToFolders:
		folder = str(k[0]) + "x" + str(k[1])
		if not os.path.isdir(argv[1] + os.path.sep + folder):
			os.mkdir(argv[1] + os.path.sep + folder)
		
	for k,v in mapToFolders.iteritems():
		folder = str(k[0]) + "x" + str(k[1])
		for x in v:
			if not os.path.exists(os.path.abspath(argv[1]) + os.path.sep + folder + os.path.sep + os.path.basename(x)):
				os.rename( x, os.path.abspath(argv[1]) + os.path.sep + folder + os.path.sep + os.path.basename(x) )
					
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
	
	sortImgToMap(argv[1])
	sortImgToDirs()