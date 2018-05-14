str = "hello world"
str = str.split(" ")
length = len(str[0])-1
print(str)

print(str[0][0])
#str[0][0] = 'e'

str2 = str[::-1]
#print(str2)
str2 = list(str2)
str2[0], str2[len(str2)-1] = str2[len(str2)-1], str2[0]
print(str2)

#for i in str2:
#    print(i, end="")


a="123"
if type(a) == type("a"):
    print("string")

test = int(a)

if type(test) == type("a"):
    print("string")

str13 = "123"
k = list(str13).pop()
#print(k)
#print(str13)
#print(list(str13).pop())

#df = pd.DataFrame(data)
#df1 = df.drop(df.columns[1], axis=1)
#df1 = df1.drop(df1.columns[2:11], axis=1)
#df1 = df1.drop(df1.columns[3:], axis=1)


r = 1.23
#r = str(r)

#k = list(r).pop()
#print(k)
#print(r)
#print(list(r).pop())

s="123"
q="455"
print(s+q)
q+="!!"
print(q)


