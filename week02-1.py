str = input("輸入一串數字：")
str = str.split(" ")
visited = [False]*len(str)
ans = ['']*len(str)


def dfs(index):
    if index == len(str):
        print(" ".join(ans))
        return

    for i in range(0,len(str)):
        if visited[i] == True:
            continue
        visited[i] = True
        ans[index] = str[i]
        #print(visited)
        #print("layer: %d  num: %d" % (index, i+1))
        #print()
        dfs(index+1)
        visited[i] = False

dfs(0)