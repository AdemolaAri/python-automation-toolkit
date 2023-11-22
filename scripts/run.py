#!/usr/bin/env python3

import os
import glob
import requests


def process_texts(path) :
    '''
         process the .txt files in the path directory and save them
         in a data structure so that you can then upload them via JSON
    '''
    data = []
    for text_file in glob.glob(path + "*.txt"):
        with open(text_file) as tf:
            files = tf.readlines()
            fname = os.path.basename(text_file).replace('txt', 'jpeg')

            curr_data = {
                "name" : files[0].strip('\n '),
                "weight" : files[1][: -4],
                "description" : files[2].strip('\n '),
                "image_name" : fname
            }
            data.append(curr_data)
    return data

def upload_texts(data, url):
    '''
        Iterate over all the data and use post method to upload all the data to the URL 
    '''
    response = requests.get(url)
    if not response.ok:
        print("Connection Error")
        return
    for file in data:
        print(f"Uploading >> {file['image_name']}")
        r = requests.post(url, json=file)
    print("============ALL DONE===========")

def main():
    '''  put it all together  '''
    IP_Address = '35.184.19.59'
    path = os.getcwd() + "/supplier-data/descriptions/"
    url = f"http://{IP_Address}/fruits/"

    if not os.path.exists(path) :
        print(f"Invalid path >> {path}")
        return
    data = process_texts(path)
    upload_texts(data, url)

if __name__ == "__main__":
    main()

