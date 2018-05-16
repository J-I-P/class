with open('ch04_file2.txt', 'r', encoding='UTF-8') as f:
    doc = f.readlines()
    print(doc)

f = open('ch04_file2.txt', 'r', encoding='UTF-8')
str1 = f.read(5)
print(str1)
f.close()