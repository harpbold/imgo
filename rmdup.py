#!/usr/bin/env python

import os
import hashlib
from sys import exit, argv
from collections import defaultdict

fileSizes = defaultdict(list)
printDeleted = False
recursive = False
imgOnly = False
imgExt = ['.jpg', '.png', '.gif']

def help():
	print "Deletes all duplicate files!"
	print "Usage: rmdup path [switches]"
	print "Switches:"
	print "\t-h, -H, -help: \tPrints the help message"
	print "\t-r, -R: \tRemoves dupes from subdirectories too with recursion"
	print "\t-w, -W: \tPrints the files which are being removed"
	print "\t-f, -F: \tOnly deletes files which has image extensions"
	exit(0)
	
def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "r+b") as f:
        for block in iter(lambda: f.read(blocksize), ""):
            hash.update(block)
    return hash.hexdigest()

def findDuplicates(dir):
	global fileSizes
	for filename in os.listdir(dir):
		act = dir + os.path.sep + filename
		if os.path.isdir(act):
			if recursive:
				findDuplicates(act)
		else:
			if imgOnly:
				ext = os.path.splitext(act)[-1].lower()
				if ext not in imgExt:
					continue
	
			fileSizes[os.stat(act).st_size].append(act)
			
def removeDuplicates():
	for size, files in fileSizes.iteritems():
		if len(files) > 1:
			for f1 in list(files):
				if f1 not in files:
					continue
				hash1 = md5sum(f1)
				for f2 in list(files):
					if f2 not in files:
						continue
					if f1 == f2:
						continue
					hash2 = md5sum(f2)
					if hash1 == hash2:
						files.remove(f2)
						os.remove(f2)
						if printDeleted:
							print f2, "has been deleted!"
					
if __name__ == "__main__":
	if len(argv) == 1:
		print "You must provide the desired path!"
		exit(-1)
		
	path = argv[1]
		
	if not os.path.exists(path):
		if path == '-h' or path == '-help':
			help()
		else:
			print "The " + os.path.abspath(path) + " does not exists!"
			print "Aborting script!"
			exit(-1)
		
	for x in argv[2:]:
		if x in ('-h', '-H', '-help'):
			help()
			exit(0)
		elif x in ('-r', '-R'):
			recursive = True
		elif x in ('-w', '-W'):
			printDeleted = True
		elif x in ('-f', '-F'):
			imgOnly = True
		else:
			print "Unknonw switch, aborting script!"
			exit(-1)
		
	print "This will delete all duplicates from " + os.path.abspath(argv[1])
	if recursive:
		print "  and all it's subdirectories"

	while 1: 
		proceed = raw_input("Proceed? y/n: ")
		if proceed in ('y', 'Y', 'n', 'N'):
			break
		
	if proceed in ('y', 'Y'):
		findDuplicates(argv[1])
		removeDuplicates()
	else:
		print "script aborted"