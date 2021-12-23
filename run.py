#! /usr/bin/env python3

import os
from os import listdir
import requests


url = "http://34.71.218.134/fruits/"
dir = "supplier-data/descriptions/"
list_files = [f for f in listdir(dir)]

for file in list_files:

 types = ["name","weight","description","image_name"]
 data = {}
 with open(dir + file, "r") as txtfile:
  x = 0
  for line in txtfile:
            data[types[x]] = line.rstrip('\n')
            x += 1
  for key in ["weight"]:
    data["weight"] = data["weight"].strip(" lbs")
    data["weight"] = int(data["weight"])
 data["image_name"] = (file.strip('.txt'))+'.jpeg'
 print(data)
 response = requests.post(url,json=data)
 if not response.status_code == 201:
  print('Something went wrong')

