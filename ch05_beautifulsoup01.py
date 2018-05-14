import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser') #html.parser解析原始碼
