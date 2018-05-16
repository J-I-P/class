def menu():
    os.system("cls")
    print("帳號密碼管理系統")
    print("-------------------------")
    print("1. 輸入帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修改密碼")
    print("4. 刪除帳號、密碼")
    print("0. 結束程式")
    print("-------------------------")

def ReadData():
    with open('ch04_password.txt', 'r', encoding='UTF-8') as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()

def disp_data():
    print("帳號 \t 密碼")
    print("=========================")
    for key in data:
        print("{}\t{}".format(key, data[key]))
    input("按任意鍵返回主選單")


def input_data():
    while True:
        name = input("請輸入帳號（Enter==>停止輸入）")
        if name=="": break
        if name in data:
            print("{}帳號已存在！".format(name))
            continue

        password = input("請輸入密碼：")
        data[name] = password
        with open('ch04_password.txt', 'w', encoding='UTF-8') as f:
            f.write(str(data))
            print("{}已被儲存完畢".format(name))
            break

def edit_data():
    while True:
        name = input("請輸入要修改的帳號（Enter==>停止輸入）")
        if name=="": break
        if not name in data:
            print("{}帳號不存在！".format(name))
            continue

        print("原來密碼為：{}".format(data[name]))
        password = input("請輸入新密碼：")
        data[name] = password
        with open('ch04_password.txt', 'w', encoding='UTF-8') as f:
            f.write(str(data))
            input("密碼更改完畢，請按任意鍵返回主選單")
            break

def delete_data():
    while True:
        name = input("請輸入要刪除的帳號（Enter==>停止輸入）")
        if name == "": break
        if not name in data:
            print("{}帳號不存在！".format(name))
            continue

        print("確定刪除 {} 的資料！".format(name))
        yn = input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            del data[name]
            with open('ch04_password.txt', 'w', encoding='UTF-8') as f:
                f.write(str(data))
                input("已刪除完畢，請按任意鍵返回主選單")
                break


import os, ast

data = dict()
data = ReadData()

while True:
    menu()
    choice = int(input("請輸入你的選擇："))
    print()
    if choice==1:
        input_data()
    elif choice==2:
        disp_data()
    elif choice==3:
        edit_data()
    elif choice==4:
        delete_data()
    else:
        break

print("程式執行完畢！")