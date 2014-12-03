#!/usr/bin/env python

from sys import argv, exit
import os

import rmdup
import extfix
import ordimg

def help():
	print "imgo - Image Organizer"
	print "Usage: imgo path [switches]"
	print "# Deletes all duplicate files"
	print "# Fixes the extension of images"
	print "# Sorts images to folders by dimension"
	print "Switches:"
	print "  -h, -H, -help: Prints the help message"
	print "  -r, -R:\t Operate on subdirectories too"
	exit(0)
	
def organizeImages(dir):
	rmdup.findDuplicates(dir)
	rmdup.removeDuplicates()
	extfix.extensionFix(dir)
	ordimg.sortImgToMap(dir)
	ordimg.sortImgToDirs()

if __name__ == "__main__":
	if len(argv) == 1:
		print "You must provide a path!"
		print "use the -h switch for help."
		
	path = argv[1]
	
	if not os.path.exists(path):
		if argv[1] == '-h' or argv[1] == '-H' or argv[1] == '-help':
			help()
		print "Provided path " + os.path.abspath(path) + " does not exists!"
		print "Aborting script"
		exit(-1)
	
	for x in argv[2:]:
		if x in ('-r', '-R'):
			rmdup.recursive = True
			extfix.recursive = True
			ordimg.recursive = True
		elif x in ('-h', '-H', '-help'):
			help()
			
	organizeImages(path)