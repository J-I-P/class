import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

#print(sp.find('title'))
#print(sp.find_all('a'))

data1 = sp.find("a", {"href":"/3th_lotto/3D/history.aspx"})
#print(data1)
#print(data1.text)


html_doc = """
<html><head><title>網頁標題</title></head>

<p class="title"><b>文件標題</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http:// example.com.elsie" class="sister" id="link1">Elsie</a>,
<a href="http:// example.com.lacie" class="sister" id="link2">Lacie</a> and
<a href="http:// example.com.tillie" class="sister" id="link3">Tillie</a>;
and they lived at bottom of a well.</p>

<p class="story">...</p>

"""
sp1 = BeautifulSoup(html_doc, 'html.parser')
print(sp1.find('b'))

print(sp1.find_all('a'))

print(sp1.find_all("a", {"class":"sister"}))

data2 = sp1.find("a", {"href":"http:// example.com.elsie"})
print(data2.text)

data3 = sp1.find("a", {"id":"link2"})
print(data3.text)
print(data3.get("href")) #取得屬性內容

data4 = sp1.select("#link3")
print(data4[0].text)

print(sp1.find_all(['title', 'a'])) #可以找尋多個標籤