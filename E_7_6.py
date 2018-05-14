#E_7_6.py功能: readlines()配合for每次取出串列並忽略表頭
with open('oil.txt', 'r', encoding='big5') as fin:
    #print(fin.readlines())
    for line in fin.readlines(): 
        if line.startswith('日'):  #判断表頭的第1個字  
            continue 
        print('---',line, end='')