print("輸入國中會考成績")
chinese = int(input("國文："))
english = int(input("英文："))
math = int(input("數學："))
society= int(input("社會："))
nature = int(input("自然："))

subject = ["國文", "英文", "數學", "社會", "自然"]
score = [chinese, english, math, society, nature]

sumA=sumB=sumC=0
type=""

for i in range(0, 5):
    if score[i] >= 85:
        sumA += 1
        if score[i] <= 90:
            type = "A"
        elif score[i] <= 94:
            type = "A+"
        else:
            type = "A++"

    elif score[i] >= 42:
        sumB += 1
        if score[i] <= 63:
            type = "B"
        elif score[i] <= 71:
            type = "B+"
        else:
            type = "B++"

    else:
        sumC += 1
        type = "C"

    print("%s： %s" % (subject[i], type))

print("等級：", end="")
if sumA != 0:
    print("%dA" % sumA, end="")
if sumB != 0:
    print("%dB" % sumB, end="")
if sumC != 0:
    print("%dC" % sumC, end="")