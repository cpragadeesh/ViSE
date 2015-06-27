#!/usr/bin/env python3

'''
	Here's how you upload an image. For this example, put the cutest picture
	of a kitten you can find in this script's folder and name it 'Kitten.jpg'

	For more details about images and the API see here:
		https://api.imgur.com/endpoints/image
'''

# Pull authentication from the auth example (see auth.py)
from auth import authenticate
from datetime import datetime
import os

album = None # You can also enter an album ID here
image_path = 'images/'

def upload_kitten(client):
	'''
		Upload a picture of a kitten. We don't ship one, so get creative!
	'''

	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'album': album,
		'name':  'Catastrophe!',
		'title': 'Catastrophe!',
		'description': 'Cute kitten being cute on {0}'.format(datetime.now())
	}

        urllist = []
	print("Uploading image... ")
	#image = client.upload_from_path(image_path, config=config, anon=False)
        for img in os.listdir(image_path):
                if img.endswith('jpg') or img.endswith('png'):
                        print "Uploading path " + image_path + img 
                        image = client.upload_from_path(image_path + img, config=config, anon=False)
                        urllist.append(image['link'])
        
	return urllist


# If you want to run this as a standalone script
def upload():
	client = authenticate()
	urllist = upload_kitten(client)

        print urllist
        
        return urllist

upload()
