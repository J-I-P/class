list = [30, 98, 12, 191, 66, 47, 82, 54]

for i in range(0, len(list)-1):
    minIndex = i
    for j in range(i, len(list)):
        if list[minIndex] > list[j]:
            minIndex = j

    if minIndex != i:
        list[i], list[minIndex] = list[minIndex], list[i]

print(list)