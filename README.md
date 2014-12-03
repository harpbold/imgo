imgo
====

Image Organizer (removes duplicates, fixes extensions and sorts to directories by dimension)

This script has been seperated to 4 scripts for people who only needs one functionality. The software uses the fork of the Python Imaging Library (PIL) called Pillow.


rmdup.py
====

Deletes all duplicate files.

Switches:

+ -h, -H, -help: Prints the help message
+ -r, -R: Removes duplicates from subdirectories too
+ -w, -W: Prints the files which are being removed
+ -f, -F: Only deletes files with image extensions


Usage:
rmdup.py [path to dir] [switches]


extfix.py
====

Fixes extension for badly named images.

Switches:
+ -h, -H, -help: Prints help message
+ -r, -R: Operates on subdirectories too

Usage:
extfix.py [path to dir] [switches]


ordimg.py
====

Moves images to folders by their dimensions. The directories will be generated to the given path (first argument).

Switches:
+ -h, -H, -help: Prints help message
+ -r, -R: Operates on subdirectories too

Usage:
ordimg.py [path to dir] [switches]


imgo.py
====

imgo (Image Organizer)
runs rmdup.py, exfix.py and ordimg.py.

Switches:
+ -h, -H, -help: Prints help message
+ -r, -R: Operates on subdirectories too

Usage:
imgo.py [path to dir] [switches]
