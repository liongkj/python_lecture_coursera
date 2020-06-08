import urllib.error
import urllib.parse
import urllib.request
import ssl
import re
from bs4 import BeautifulSoup
url = "http://py4e-data.dr-chuck.net/known_by_Leydon.html"

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
position = input("Position: ")
count = input("Count: ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieve all of the anchor tags

c = 0

names = []


def fetch(url, c, names):

    if(c < int(count)):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')

        third = tags[int(position) - 1]
        link = third.get('href', "None")
        names.append(third.text)
        print(link)
        c += 1
        return fetch(link, c, names)


fetch(url, c, names)
print(' '.join(names))
