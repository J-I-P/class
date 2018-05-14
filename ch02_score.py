nat = input("請輸入國文成績：")
math = input("請輸入數學成績：")
eng = input("請輸入英文成績：")
sum = int(nat) + int(math) + int(eng)
average = sum / 3
print("成績總分：%d，平均成績：%5.2f" % (sum, average))