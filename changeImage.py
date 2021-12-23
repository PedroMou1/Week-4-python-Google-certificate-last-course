#!/usr/bin/env python3

# importing modules
import os
from os import listdir
import sys
# importing Image module from PIL library(currently pillow)
from PIL import Image

dir = "/home/student-01-dedb6c4fb424/supplier-data/images/"

# with this function you go through each one of the files in the old directory and then pick the ones that end with ".tiff_" as they are images:
img_files = [f for f in listdir(dir) if f.endswith(".tiff")]

for file in img_files:
    src_img = Image.open(dir + file)

    new_img = src_img.resize((600,400))

    # NOTE: we need to convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")

    image_path = dir + file
    path = os.path.splitext(image_path)[0]
    new_path = '{}.jpeg'.format(path)


    new_img.save(new_path, "JPEG")

