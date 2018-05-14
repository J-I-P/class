import os
cur_path = os.path.dirname(__file__)

os.system("clear")
os.system("mkdir dir2")
os.system("cp ch04_ossystem.py dir2/copyfile.py")
file = cur_path + "/dir2/copyfile.py"
os.system("cat " + file)

