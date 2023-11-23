#!/usr/bin/env python3

import os
import glob
from PIL import Image


def resize_images(path: str, img_size: tuple):
    """
    Resize all images within the specified path to the given resolution.

    Args:
        path (str): The path of the directory containing images.
        img_size (tuple): A tuple representing the desired size (width, height).
    """
    for img_file in glob.glob(path + "*.*"):
        try:
            with Image.open(img_file) as img:
                print("\u2713 |Processing...")
                new_fname = os.path.basename(img_file)
                img = img.convert("RGB")
                img = img.resize(img_size) if img_size else img
                img.save(path + new_fname)
                print(f"...resized <<{img_file}>>")
        except Exception as e:
            print(f"\u2717 |Unable to resize----{e}|")
    print("==============DONE==============")


def main():
    """
    Main function to interact with the user, providing input for the conversion process.
    """
    path = input("Enter the path: ")
    size_str = input("Enter the desired size (width,height) eg. 200,400: ")
    img_size = tuple(map(int, size_str.split(",")))

    if os.path.exists(path):
        resize_images(path, img_size)
    else:
        print(f" Path <{path}> does not exist")


if __name__ == "__main__":
    main()
