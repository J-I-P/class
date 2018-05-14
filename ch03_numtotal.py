sum = 0
n = int(input("請輸入正整數："))
for i in range(1, n+1):
    sum += i
print("1 到 %d 的" % n, end="")

list = ["整", "數", "和", "為", "："]
for i in list:
    print(i, end="")
print(sum)