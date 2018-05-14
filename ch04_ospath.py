import os.path as ospath
cur_path = ospath.dirname(__file__)
print("目前路徑：" + cur_path)
filename = ospath.abspath("ch04_ospath.py")
if ospath.exists(filename):
    print("完整路徑名稱：" + filename)
    print("檔案大小：" + str(ospath.getsize(filename)))

    basename = ospath.basename(filename)
    print("最後的檔案或路徑名稱：" + basename)

    dirname = ospath.dirname(filename)
    print("目前檔案目錄路徑：" + dirname)

    print("是否為目錄：" + str(ospath.isdir(filename)))

    fullpath, fname = ospath.split(filename)
    print("目錄名稱：" + fullpath)
    print("檔名：" + fname)

    Drive, fpath = ospath.splitdrive(filename)
    print("磁碟機：" + Drive)
    print("路徑名稱" + fpath)

    fulllpath = ospath.join(fullpath + "//" + fname)
    print("組合路徑：" + fullpath)