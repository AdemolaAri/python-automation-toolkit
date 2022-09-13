#!/usr/bin/env python3

import requests
import os
import glob

def upload_images(img_path, url):
    '''
        takes the jpeg images from img_path directory and uploads them to 
        the url web server.
    '''
    for image in glob.glob(img_path + "*.jpeg"):
        with open(image, 'rb') as img:
            print(f"Uploading >> {image}")
            r = requests.post(url, files= {'file': img})
            print(f"\tStatus Code : {r.status_code}")

def main():
    ''' main function to put it all together '''
    path = os.getcwd() + "/supplier-data/images/"
    url  = "http://localhost/upload/"
    
    url_connects = requests.get(url).ok
    if os.path.exists(path) and url_connects:
        upload_images(path, url)
        return
    print(f" Invalid PATH or URL \n Path >> {path} \n Url >> {url} ")


if __name__ == "__main__":
    main()