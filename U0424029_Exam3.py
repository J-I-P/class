import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data = sp.select("#rightdown") #select 回傳串列
#print(len(data)) #長度1
#print(data)


#4星彩
print()
data10 = data[0].find_all("div", {"class":"contents_box04"})
data10_date = data10[1].find("span", {"class":"font_black15"})
print("\n4星彩 %s" % data10_date.text)
data10_1 = data10[1].find_all("div", {"class":"ball_tx"})

print("中獎號碼：", end="")
for i in data10_1:
    print(i.text, end=" ")