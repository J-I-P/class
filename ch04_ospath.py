import os.path as ospath
cur_path = ospath.dirname(__file__)
print("目前路徑：" + cur_path)
filename = ospath.abspath("ch04_ospath.py")
if ospath.exists(filename):
    print("完整路徑名稱：" + filename)
    print("檔案大小：" + ospath.getsize(filename))

    basename = ospath.basename(filename)
    print("最後的檔案或路徑名稱：" + basename)

    dirname = ospath.dirname(filename)
    print("目前檔案目錄路徑：" + dirname)

