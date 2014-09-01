#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import os
import cgitb
import cgi
import json
cgitb.enable()

# The base path where your content is.  This should be set to '.' if content is in the same directory as the script.
BASE_PATH="../"

# And this is the URL needed to access the same path on your web server.
BASE_URL ="http://"+os.environ['SERVER_NAME']+"/video/"

#cgi.print_environ()

directory_arg = os.environ['REQUEST_URI'][len(os.environ['SCRIPT_NAME']):]

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
    
    dirnames.sort()
        
    for dirname in dirnames:
            directories.append( {"title" : dirname , "directory" : [base_arg + dirname] } )
            
    filenames.sort()
    
    for filename in filenames:
        if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".mkv"):
            videos.append( {"title" : filename , "sources" : [BASE_URL + base_arg + "/" + filename] } )
    # Break here as we are only interested in the top level directory.
    break
    
data = { "videos" : videos , "directories" : directories}

print(json.dumps(data))
print("")