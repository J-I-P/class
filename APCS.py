# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 18:36:05 2018

@author: User
"""
import requests,re

url = 'https://www.caac.ccu.edu.tw/CacLink/apply107/107apply_Sieve_pg58e3q/html_sieve_107yaya/ColPost/common/apply/' 
name=['師大','政大','中央']
school=['002212','006372','016202']

def APCS(url):
    html = requests.get(url)
    regex=re.compile('[0-9]{8}') # 連續8位數字(準考證號碼)
    data=regex.findall(html.text)
    for i in range(0,len(data)):
       print(data[i],end=' ')
    print()

for i in range(0,3):
    print("%s APCS 組:"%name[i])
    nurl=url+school[i]+'.htm'
    APCS(nurl)
