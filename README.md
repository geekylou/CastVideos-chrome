# CastVideos-chrome
===============================

This is modified version of the Chromecast demo app which can be used to cast your video collection from a web server on your PC/NAS or web site to a Chromecast.  

## Setup Instructions

# Pre-requisites
 1. Get a Chromecast device
 2. Install appropriate Chrome browser
 3. Install appropriate Chrome Cast extension

 See the developer guide and release notes at https://developers.google.com/cast/ for more details.
 
# Steps:
 1. Put all files on your own server.  This server can be on your local network or PC if you don't want the site accessible to the internet.
 2. Setup your web server so that it can execute python CGI scripts.
 3. Change the BASE_URL value at the top of the getDirectoryListing.py file to point to the URL of your video library.
 4. Open a browser and point to your page at http://[YOUR_SERVER_LOCATION]/CastVideos-chrome/

# Developer stuff from the demo app.
##Documentation
* Cast APIs: http://developers.google.com/cast/docs/chrome_sender

## References and How to report bugs
* Cast APIs: http://developers.google.com/cast/docs/reference/chrome
* Design Checklist (http://developers.google.com/cast/docs/design_checklist)
* If you find any issues, please open a bug here on GitHub

How to make contributions?
Please read and follow the steps in the CONTRIBUTING.md

License
See LICENSE.md

## Google+
 Google Cast Developers Community on Google+ [http://goo.gl/TPLDxj](http://goo.gl/TPLDxj)
