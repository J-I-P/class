import requests,re

url = 'https://www.caac.ccu.edu.tw/CacLink/apply107/107apply_Sieve_pg58e3q/html_sieve_107yaya/ColPost/common/apply/'
name=['師大','政大','中央']
school=['002212','006372','016202']

def APCS(url, id):
    html = requests.get(url)
    regex=re.compile('[0-9]{8}') # 連續8位數字(準考證號碼)
    data=regex.findall(html.text)
    for i in range(0,len(data)):
        if data[i]==id:
            return True
    return False

    print()

myid = input("准考證號碼：")

for i in range(0,3):
    nurl=url+school[i]+'.htm'
    if APCS(nurl, myid):
        print("%s :錄取" % name[i])
    else:
        print("%s :不錄取" % name[i])
