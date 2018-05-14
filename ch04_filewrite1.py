content='''Hello Python
中文字測試
Welcome
'''

f = open('ch04_file1.txt', 'w')
f.write(content)
f.close()