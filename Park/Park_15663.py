N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

totalList = []

def recur(arr, newList, cnt):
    if cnt==M:
        # if(newList not in totalList):
        #     totalList.append(newList)
        for i in range(len(newList)):
            print(newList[i], end=" ")
        print()
        cnt-=1
        return


    # 아래 방법은 맹진 방법 쪼까 참고했슈,,,
    # 내가 하려던 방법으로 하니깐 시간 초과가 뜨더라궁
    for i in sorted(set(arr)):  # 집합형으로 바꾸고 정렬시킴
        newList.append(i)
        index = arr.index(i)
        recur(arr[:index]+arr[index+1:], newList, cnt+1)    # 이거 아주 정말 획기적인 방법
        newList = newList[:cnt]


recur(array, [], 0)
