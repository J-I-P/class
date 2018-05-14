import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data = sp.select("#rightdown") #select 回傳串列
#print(len(data)) #長度1
#print(data)

#Bingo
data1 = data[0].find("div", {"class":"contents_box01"})
#print(data1)
data1_date = data1.find("span", {"class":"font_black15"})
print("Bingo %s" % data1_date.text)
data1_1 = data1.find_all("div", {"class":"ball_yellow"})
#print(data1_1) #串列

print("開出獎號：", end="")
for i in data1_1:
    print(i.text, end=" ")

print("\n超級獎號：", end="")
data1_2 = data1.find("div", {"class":"ball_red"})
print(data1_2.text)

print("猜大小：", end="")
data1_3 = data1.find("div", {"class":"ball_blue_BB1"})
print(data1_3.text)

print("猜大小：", end="")
data1_4 = data1.find("div", {"class":"ball_blue_BB2"})
print(data1_4.text)

#威力彩
data2 = data[0].find_all("div", {"class":"contents_box02"})
data2_date = data2[0].find("span", {"class":"font_black15"})
print("\n威力彩 %s" % data2_date.text)
data2_1 = data2[0].find_all("div", {"class":"ball_green"})

print("開出順序：", end="")
for i in range(len(data2_1)-6):
    print(data2_1[i].text, end=" ")

print("\n大小順序：", end="")
for i in range(6,len(data2_1)):
    print(data2_1[i].text, end=" ")

print("\n第二區：", end="")
data2_3 = data2[0].find("div", {"class":"ball_red"})
print(data2_3.text)

#38樂合彩
data2 = data[0].find_all("div", {"class":"contents_box02"})
data3_date = data2[1].find("span", {"class":"font_black15"})
print("\n38樂合彩 %s" % data2_date.text)
data3_1 = data2[1].find_all("div", {"class":"ball_green"})

print("開出順序：", end="")
for i in range(len(data3_1)-6):
    print(data3_1[i].text, end=" ")

print("\n大小順序：", end="")
for i in range(6,len(data3_1)):
    print(data3_1[i].text, end=" ")
print()

#大樂透
data2 = data[0].find_all("div", {"class":"contents_box02"})
data4_date = data2[2].find("span", {"class":"font_black15"})
print("\n大樂透 %s" % data4_date.text)
data4_1 = data2[2].find_all("div", {"class":"ball_yellow"})

print("開出順序：", end="")
for i in range(len(data4_1)-6):
    print(data4_1[i].text, end=" ")

print("\n大小順序：", end="")
for i in range(6,len(data4_1)):
    print(data4_1[i].text, end=" ")

print("\n特別號：", end="")
data4_3 = data2[2].find("div", {"class":"ball_red"})
print(data4_3.text)

#49樂合彩
data2 = data[0].find_all("div", {"class":"contents_box02"})
data5_date = data2[3].find("span", {"class":"font_black15"})
print("\n49樂合彩 %s" % data2_date.text)
data5_1 = data2[3].find_all("div", {"class":"ball_yellow"})

print("開出順序：", end="")
for i in range(len(data5_1)-6):
    print(data5_1[i].text, end=" ")

print("\n大小順序：", end="")
for i in range(6,len(data5_1)):
    print(data5_1[i].text, end=" ")
print()

#大福彩
data6 = data[0].find("div", {"class":"contents_box05"})
data6_date = data6.find("span", {"class":"font_black15"})
print("\n大福彩 %s" % data6_date.text)
data6_1 = data6.find_all("div", {"class":"ball_tx"})

print("開出順序：", end="")
for i in range(len(data6_1)-7):
    print(data4_1[i].text, end=" ")

print("\n大小順序：", end="")
for i in range(7,len(data6_1)):
    print(data6_1[i].text, end=" ")

print("\n特別號：", end="")
data6_3 = data6.find("div", {"class":"ball_red"})
print(data6_3.text)

#今彩539
data7 = data[0].find_all("div", {"class":"contents_box03"})
data7_date = data7[0].find("span", {"class":"font_black15"})
print("\n今彩539 %s" % data7_date.text)
data7_1 = data7[0].find_all("div", {"class":"ball_tx"})

print("開出順序：", end="")
for i in range(len(data7_1)-5):
    print(data7_1[i].text, end=" ")

print("\n大小順序：", end="")
for i in range(5, len(data7_1)):
    print(data7_1[i].text, end=" ")

#39樂合彩
print()
data8 = data[0].find_all("div", {"class":"contents_box03"})
data8_date = data8[1].find("span", {"class":"font_black15"})
print("\n39樂合彩 %s" % data8_date.text)
data8_1 = data8[1].find_all("div", {"class":"ball_tx"})

print("開出順序：", end="")
for i in range(len(data8_1)-5):
    print(data8_1[i].text, end=" ")

print("\n大小順序：", end="")
for i in range(5, len(data8_1)):
    print(data8_1[i].text, end=" ")
print()

#3星彩
data9 = data[0].find_all("div", {"class":"contents_box04"})
data9_date = data9[0].find("span", {"class":"font_black15"})
print("\n3星彩 %s" % data9_date.text)
data9_1 = data9[0].find_all("div", {"class":"ball_tx"})

print("中獎號碼：", end="")
for i in data9_1:
    print(i.text, end=" ")

#4星彩
print()
#data10 = data[0].find_all("div", {"class":"contents_box04"})
data10_date = data9[1].find("span", {"class":"font_black15"})
print("\n4星彩 %s" % data10_date.text)
data10_1 = data9[1].find_all("div", {"class":"ball_tx"})

print("中獎號碼：", end="")
for i in data10_1:
    print(i.text, end=" ")