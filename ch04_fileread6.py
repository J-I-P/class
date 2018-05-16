f = open('ch04_file2.txt', 'r', encoding='UTF-8')
print(f.readline())
print(f.readline(3))
f.close()