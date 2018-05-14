str = input("輸入需被加密的字串：")

list = str.split(" ")
ans =""

#for i in range(0, len(list)):
#    length = len(list[i])-1
#    middle = list[i][length-1:0:-1]
    #print(middle)
#    if(len(list[i])>1):
#        ans += list[i][0]+middle+list[i][length]
#    else:
#        ans += list[i][0]


#for word in list:
#    length = len(word)-1
#    middle = word[length-1:0:-1]
#    if len(word)>1:
#        ans += word[0]+middle+word[length]
#    else:
#        ans += word[0]

for w in list:
    tmp = w[::-1]
    #print(tmp)
    for i in range(len(w)):
        if i==0:
            ans += tmp[len(w)-1]
        elif i==len(w)-1:
            ans += tmp[0]
        else:
            ans += tmp[i]

print(ans)