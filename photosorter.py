#!/usr/bin/python3

from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil

directory = "/home/trev/Pictures/oldpics/"
examplefile = ""
#yearfolder = ""

def extractyear(exifdata):
        yeartaken = ""
        try:
            for tag_id in exifdata:
    	# get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
    # decode bytes
                if isinstance(data, bytes):
                    data = data.decode()
                if "DateTimeOriginal" in f"{tag:25}":
                    #print(f"{data}"[0:4])
                    yeartaken = f"{data}"[0:4]
                #print(f"{tag:25}: {data}")
    #bob = f"{tag:25}"
    #print (bob)

        except:
            pass

        return yeartaken


for entry in os.scandir(directory):
    if (entry.path.endswith(".jpg") or entry.path.endswith(".JPG") or entry.path.endswith(".jpeg") and entry.is_file()):
        #print(entry.path) 
        image = Image.open(entry.path)
        exifdata = image.getexif()
        yearfolder = extractyear(exifdata)
        
        
#create the directory to put piccies in
        destpath = "/nfs/pictures/" + yearfolder + "/trev_recovered"
        try:
            print ("making the dir: " + destpath) 
            os.mkdir(destpath)
        except:
            print("Already exists...continuing")


        try:
            print("Moving " + entry.path + " to " + destpath + "/" + os.path.basename(entry.path) + "\n")
            shutil.move(entry.path, destpath + "/" + os.path.basename(entry.path))
        except:
            pass

