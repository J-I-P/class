import os, shutil

cur_path = os.path.dirname(__file__)
destfile = cur_path + "//" + "ch04_newfile.py"
shutil.copy("ch04_shutil.py", destfile)