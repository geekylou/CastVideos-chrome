#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

# The base path where your content is.  This should be set to '.' if content is in the same directory as the script.
BASE_PATH="../videos"

import os
import cgitb
import cgi
import json
cgitb.enable()

print("Content-Type: application/json")
print("")
    
arguments = cgi.FieldStorage()

directory_arg = arguments.getvalue("directory")

# Guard against the script being used to get directory listings of directories below the base.
if directory_arg and directory_arg.find("..") > 0:
    directory_arg = None

if directory_arg:
    path = BASE_PATH + "/" + directory_arg
else:
    path = BASE_PATH
    
videos = []
directories = []

for (dirpath, dirnames, filenames) in os.walk(path):
    if directory_arg:
        base_arg = directory_arg + "/"
        
        if directory_arg.rfind('/') > 0:
            directories.append( {"title" : ".." , "directory" : directory_arg[:directory_arg.rfind('/')] } )
        else:
            directories.append( {"title" : ".." , "directory" : "" } )        
    else:
        base_arg = ""
        
    for dirname in dirnames:
            directories.append( {"title" : dirname , "directory" : [base_arg + dirname] } )
    for filename in filenames:
        if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".mkv"):
            videos.append( {"title" : filename , "sources" : [BASE_PATH + "/" + filename] } )
    break
    
data = { "videos" : videos , "directories" : directories}

print(json.dumps(data))
print("")