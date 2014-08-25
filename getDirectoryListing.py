#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
from os import walk
import cgitb
import json
cgitb.enable()

print("Content-Type: application/json")
print("")
    
# The base path where your content is.
BASE_PATH="../videos"

videos = []

for (dirpath, dirnames, filenames) in walk(BASE_PATH):    
    for filename in filenames:
        if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".mkv"):
            videos.append( {"title" : filename , "sources" : [BASE_PATH + "/" + filename] } )
    break
    
data = { "videos" : videos }

print(json.dumps(data))
print("")