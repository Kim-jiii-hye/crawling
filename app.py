from flask import Flask
import requests
import re
import urllib.request
from bs4 import BeautifulSoup
import json

osulloc_url = 'https://www.osulloc.com/kr/ko/shop/item/list?1=1&sort=review'

app = Flask(__name__)

@app.route('/')
def hello():
    html = urllib.request.urlopen(osulloc_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    sites = soup.find_all('div', {'class':'item'})
    return 'dddd'