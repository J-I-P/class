import os as s
dir = "myDir"
if s.path.exists(dir):
    s.rmdir(dir)
else:
    print(dir+"目錄未建立！")