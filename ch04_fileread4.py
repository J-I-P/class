with open('ch04_file1.txt', 'r') as f:
    content = f.readlines()
    print(type(content))
    print(content)