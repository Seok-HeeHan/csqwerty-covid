## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os
import time

f = open("/home/hsh060824/seokhee/교육/학년/2학년/Qwerty/covid/comfirmt.txt", 'w')
f.write(time.strftime('%Y-%m-%d', time.localtime(time.time())))
f.close()

## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://search.naver.com/search.naver?ie=UTF-8&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%EC%88%98')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'div.content_search.section > div > div > div > div.production_main > div > div.main_detail_bx > div:nth-child(2) > div > div > div > div > div > p > strong'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('href')
    #data = title.get('href')

inv_data = dict(zip([1, 2, 3, 4], (data.keys())))

with open(os.path.join(BASE_DIR, 'comfirm.json'), 'w+') as json_file:
    json.dump(inv_data, json_file)
