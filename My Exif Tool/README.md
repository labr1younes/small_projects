# My Exif Tool

This program is a tool for manipulating Exif data of Images (*.jpg) , using Pillow module in Python .
You can **show** the data or **remove** it for now through command-line arguments (CLI).

# Features
1. Show the basic information of the image , like format ,Height and Width ...etc .
2. Show the Exif data of the image , like model and DateTime ...etc .
3. Remove all the Exif data of the image , this will create a similar image but without exif data .

# How to use 
The following commands are available in myexiftool.py :
1. `-h` or `--help` : Show the help message .
2. `-sh` or `--show` : Show the basic information of the image .
3. `-exf` or `--exif` : Show the Exif data of the image .
4. `-rmv` or `--remove` : Remove all the Exif data of the image .

**Example** :\
To remove all the Exif data , run the following command:\
`python myexiftool.py  -exf dir image_with_exif.jpg`
# What is an EXIF file?

EXIF (Exchangeable Image File Format) files store important data about photographs. Almost all digital cameras create these data files each time you snap a new picture. An EXIF file holds all the information about the image itself — such as the exposure level, where you took the photo, and any settings you used.

This makes it easier to filter photos on your storage device by particular image characteristics. It’s useful for photographers to learn how to read and understand the EXIF format to make cataloging your images easier.

If you see a photo on a website that you want to find out more about, you can often access EXIF data if the website is using the original photograph file. But some people prefer to remove the EXIF file before loading their personal images to a website to protect any personal information, like their GPS location.

You might also encounter audio data like decibel range, bitrate, or mono/stereo information for any video footage in an EXIF file.


