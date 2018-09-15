#!/usr/bin/env python3
__author__ = "Hendrik Teuber"
__version__ = "0.1"
__license__ = "MIT"
__email__ = "hendrik@dd5ht.de"

import sys
import os
import urllib.request
from urllib.parse import urlparse


def main():
    """Opens the user given file and downloads the files from the given urls."""
    try:
        with open(sys.argv[1], "r") as urls:
            for url in urls:
                data = download_file(url.strip("\n"))
                if data != None:
                    file_name = get_file_name(url)
                    save_file(file_name, data)
    except IndexError:
        print("You need to use at least one argument eg. $ ./image_downloader.py sample.txt")
    except IOError:
        print("We cant open the given file")


def download_file(url):
    """Return the data for the given url"""
    try:
        with urllib.request.urlopen(url) as response:
            print("Downloading: " + url)
            return response.read()
    except:
        print("Cant retrive the file with the URL: '{}' .".format(url))
        return None


def save_file(file_name, data):
    """Saves the data under the given file name"""
    try:
        with open(file_name, "wb") as out_file:
            out_file.write(data)
    except:
        print("Cant write file to filesystem!")


def get_file_name(url):
    """Return the file name for the given url: eg. example.com/sample.jpg => sample.jpg"""
    try:
        return os.path.basename(urlparse(url).path)
    except:
        print("Can't parse the given url: {}".format(url))
        return None #We just explicitly return None for clarity 


if __name__ == "__main__":
    main()
