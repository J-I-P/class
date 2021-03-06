import tkinter as tk
import requests,re


url = 'https://www.caac.ccu.edu.tw/CacLink/apply107/107apply_Sieve_pg58e3q/html_sieve_107yaya/ColPost/common/apply/'
name=['師大資工APCS組','政大資工APCS組','中央資工APCS組']
school=['002212','006372','016202']
strr = ""
def APCS(url, id):
    html = requests.get(url)
    regex=re.compile('[0-9]{8}') # 連續8位數字(準考證號碼)
    data=regex.findall(html.text)
    for i in range(0,len(data)):
        if data[i]==id:
            return True
    return False

def chkid():
    count = 0
    global strr
    for i in range(0,3):
        nurl=url+school[i]+'.htm'
        if APCS(nurl, idsearch.get()):
            count+=1
            textshow.insert(tk.END, str(idsearch.get())+" 錄取："+name[i]+'\n')
    if count>0:
        textshow.insert(tk.END, "共錄取"+str(count)+"間學校"+'\n')
    else:
        textshow.insert(tk.END, str(idsearch.get())+" 都未錄取"+'\n')

def quit():
    global win
    win.destroy()

win = tk.Tk()
win.title("查榜")
win.geometry("450x300")
idsearch = tk.StringVar()
msg = tk.StringVar()
frame1 = tk.Frame(win)
frame1.pack()
label = tk.Label(frame1, text="請輸入准考證號碼：")
enter = tk.Entry(frame1, textvariable=idsearch)
label.grid(row=0, column=0)
enter.grid(row=0, column=1)

frame2 = tk.Frame(win)
frame2.pack()
buttonS = tk.Button(frame2, text="查詢", command=chkid)
buttonEND = tk.Button(frame2, text="結束", command=quit)
buttonS.grid(row=0, column=0)
buttonEND.grid(row=0, column=1)
frame3 = tk.Frame(win)
frame3.pack()
textshow = tk.Text(frame3, fg="red")
textshow.pack()

win.mainloop()