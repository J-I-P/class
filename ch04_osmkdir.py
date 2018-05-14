import os as s
dir = "myDir"
if not s.path.exists(dir):
    s.mkdir(dir)
else:
    print(dir+"已經建立！")