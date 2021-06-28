N, M = map(int, input().split())

arr = list(range(1, N+1))

def recur(newList, cnt):
    global arr
    if(cnt==M):
        for i in newList:
            print(i, end=" ")
        print()
        cnt-=1
        return

    for i in range(len(arr)):
        newList.append(arr[i])
        recur(newList, cnt+1)
        newList = newList[:cnt] # 여기도 이게 약간 문제였음

recur([], 0)
