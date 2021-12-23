#!/usr/bin/env python3

import requests
from os import listdir
import sys
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
dir = "/home/student-01-dedb6c4fb424/supplier-data/images/"

img_files = [f for f in listdir(dir) if f.endswith(".jpeg")]


for file in img_files:
 with open(dir + file, "rb") as opened:
   r = requests.post(url, files={"file": opened})
