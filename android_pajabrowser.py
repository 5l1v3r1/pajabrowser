#!/usr/bin/python3

__author__ = "Ismael"
__copyright__ = "Copyright 2019, GuadalPING SL"
__credits__ = ["Ismael Joyera Aguilar", "Diego Gamaza", "Alejandro Santamaría"]
__license__ = "GNU/GPLv3"
__version__ = "1.0.1"
__email__ = "guadalping@gmail.com"


import requests
from bs4 import BeautifulSoup
from random import choice


print("""
              _           _                                     
 _ __   __ _ (_) __ __   | |__  _ __ _____      _____  ___ _ __ 
| '_ \ / _` || |/ _` |   | '_ \| '__/ _ \ \ /\ / / __|/ _ \ '__|
| |_) | (_| || | (_| | - | |_) | | | (_) \ V  V /\__ \  __/ |   
| .__/ \__,_|/ |\__,_|   |_.__/|_|  \___/ \_/\_/ |___/\___|_|   
|_|        |__/                                             
""")

html = requests.get("https://pornhub.com").text  # gets main page html
soup = BeautifulSoup(html, "lxml")  # soup object
things = []  # links list
for a in soup.find_all('a', href=True):  # find links
    things.append(a["href"])
links = []
for i in things:
    if "view_video" in i:  # if is valid...
        links.append(i)

link = choice(links)  # random!!!
print("Your random porn video is \"https://pornhub.com" + link + "\" enjoy!")
