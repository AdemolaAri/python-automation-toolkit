#!/usr/bin/env python3

import os
import glob
from PIL import Image


def convert_format(path: str, from_extension: str, to_extension: str):
    """
    Change the format of all images within the specified path.

    Args:
        path (str): The path of the directory containing images.
        from_extension (str): The current image format extension.
        to_extension (str): The desired image format extension.
    """
    for img_file in glob.glob(path + "*." + from_extension):
        try:
            with Image.open(img_file) as img:
                print("\u2713 |Processing...")
                new_fname = os.path.basename(img_file).replace(
                    from_extension, to_extension
                )
                img = img.convert("RGB")
                img.save(path + new_fname)
                print(f"...converted <<{img_file}>>|")
        except Exception as e:
            print(f"\u2717 |Unable to convert----{e}|")
    print("==============DONE==============")


def main():
    """
    Main function to interact with the user, providing input for the conversion process.
    """
    path = input("Enter the path: ")
    from_extension = input("Enter the current image format extension: ")
    to_extension = input("Enter the desired image format extension: ")

    if os.path.exists(path):
        convert_format(path, from_extension, to_extension)
    else:
        print(f" Path <{path}> does not exist")


if __name__ == "__main__":
    main()
