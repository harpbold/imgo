imgo
====

Image Organizer (removes duplicates, fixes extensions and sorts to directories by dimension)

This script has been seperated to 4 scripts for people who only needs one functionality. This software uses Pillow which is the fork of the Python Imaging Library (PIL).

about
====

The purpose of this software is to help you organize your images.
This script will remove any duplicate images from your image collection, rename any badly named file to it's correct extension and map images to folders by their dimension.


gui_imgo.py
====

GUI for imgo, made with PyQt4.


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

Try it out
====

I recommend using [this](http://www.reddit.com/r/pcmasterrace/comments/21xa6w/a_torrent_version_of_the_over_52000_wallpapers/) massive image collection for testing purposes.

Contributors
====

[Jabba Laci](https://github.com/jabbalaci)
