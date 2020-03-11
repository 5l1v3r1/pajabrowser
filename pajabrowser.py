#!/usr/bin/python3

__author__ = "Alejandro Santa-Weed"
__copyright__ = "Copyright 2019, GuadalPING SL"
__credits__ = ["Ismael Joyera Aguilar", "Diego Gamaza", "Alejandro Santamery"]
__license__ = "GNU/GPLv3"
__version__ = "1.0.1"
__email__ = "guadalping@gmail.com"


import requests
from bs4 import BeautifulSoup
from random import choice
from selenium import webdriver

print("""


              _           _                                     
 _ __   __ _ (_) __ __   | |__  _ __ _____      _____  ___ _ __ 
| '_ \ / _` || |/ _` |   | '_ \| '__/ _ \ \ /\ / / __|/ _ \ '__|
| |_) | (_| || | (_| | - | |_) | | | (_) \ V  V /\__ \  __/ |   
| .__/ \__,_|/ |\__,_|   |_.__/|_|  \___/ \_/\_/ |___/\___|_|   
|_|        |__/                                             


""")

proxies = {'http':'socks5h://127.0.0.1:9050', 'https':'socks5h://127.0.0.1:9050'} # tor proxy

try:
  requests.get("https://google.es", proxies=proxies)
except:
  print("Tor Not Working, use 'sudo service tor start'")
  exit()

html = requests.get("https://pornhub.com", proxies=proxies).text  # gets main page html

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

driver = webdriver.Firefox()
driver.get("https://pornhub.com" + link)  # open page
