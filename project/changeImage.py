#!/usr/bin/env python3

import os
import glob
from PIL import Image

def process_image(path):
    '''
        Process all images within path directory to the 
        following specifications:
            Size: Change image resolution from 3000x2000 to 600x400 pixel
            Format: Change image format from .TIFF to .JPEG
    '''
    for img_file in glob.glob(path + "*.tiff"):
        with Image.open(img_file) as img:
            print(f"Processing <<{img_file}>>")
            new_fname = os.path.basename(img_file).replace('tiff', 'jpeg')
            img = img.convert("RGB")
            img = img.resize((600, 400))
            img = img.save(path + new_fname, 'JPEG')
    print("===========ALL DONE==============")

def main():
    ''' main function to put everything together '''
    path = os.getcwd() + "/supplier-data/images/"
    if os.path.exists(path):
        process_image(path)
        return
    print(f" Path <{path}> does not exist")

if __name__ == "__main__":
    main()
