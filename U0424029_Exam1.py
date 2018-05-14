import requests,re

url = 'https://www.caac.ccu.edu.tw/CacLink/apply107/107apply_Sieve_pg58e3q/html_sieve_107yaya/ColPost/common/apply/'
name=['成大','交大','清大']
school=['004392','013092','011352']
data1=[]
data2=[]
data3=[]

def APCS(url, dataa):
    html = requests.get(url)
    regex=re.compile('[0-9]{8}') # 連續8位數字(準考證號碼)
    data=regex.findall(html.text)
    for i in range(0, len(data)):
        dataa.append(data[i])




nurl=url+school[0]+'.htm'
APCS(nurl, data1)
nurl=url+school[1]+'.htm'
APCS(nurl, data2)
nurl=url+school[2]+'.htm'
APCS(nurl, data3)

for item in data1:
    if item in data2:
        if item in data3:
            print(item)

#print(data1)
#print(data2)
#print(data3)
