from flask import Flask, render_template
import requests
import re
import urllib.request
from bs4 import BeautifulSoup
import json

osulloc_url = 'https://www.osulloc.com/kr/ko/shop/item/list?1=1&sort=review'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/', method=['POST'])
# def index_post():
#     html = urllib.request.urlopen(osulloc_url).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     sites = soup.find_all('div', {'class': 'item'})
#     link = soup.select_one('#pagination > a:last-child')['href']
#     totalpage = int(link.split('p=')[1])
#     return 'dddd'

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.debug = True
    app.run()