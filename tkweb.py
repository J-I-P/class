import tkinter as tk

#from tkinter import *
#root = Tk()
#root.title('hello world')
#root.mainloop()

#top=tk.Tk()                                #准备一个画布
#label=tk.Label(top,text="hello world")     #在画布上添加label组件
#label.pack()                                    #将label组件显示出来
#top.mainloop()

def click1():
    textvar.set("clicked")

win = tk.Tk()
win.geometry("450x100")
win.title("test")
#label=tk.Label(win,text="測試")     #在画布上添加label组件
textvar = tk.StringVar()
buttonC = tk.Button(win, text="確定", bg="yellow",textvariable=textvar,  command=click1)
textvar.set("按")
buttonC.pack()
#label.pack()                                    #将label组件显示出来
win.mainloop()