import glob

files = glob.glob("ch04_glob.py")+glob.glob("ch04*.py")

for file in files:
    print(file)