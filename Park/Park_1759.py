L, C = map(int, input().split())
array = list(input().split())
array.sort()

realMoeum = "aeiou"
moeum = []
for i in array:
    if i in realMoeum:
        moeum.append(i)

realList = []

def recur(arr, newList, cnt):
    if(cnt==L):
        cntMoeum = 0
        cntJaeum = 0

        for i in newList:
            if i in moeum:
                cntMoeum+=1
            else:
                cntJaeum+=1
        if cntMoeum>=1 and cntJaeum>=2:
            realList.append(newList)
        cnt-=1
        return

    for i in range(len(arr)):
        newList.append(arr[i])
        recur(arr[i+1:], newList, cnt+1)
        newList = newList[:cnt]

recur(array, [], 0)
for i in range(len(realList)):
    for j in range(L):
        print(realList[i][j], end="")
    print()
