# 내장함수 사용 X
N, M = map(int, input().split())
array = list(range(1, N+1))

# cnt는 몇 번째 단계(현재 몇 번째 자리 결정 중)인지 확인 위한 변수

def recur(arr, newList, cnt):
    if(len(newList)==M):
        for i in newList:
            print(i, end= " ")
        print()
        cnt -= 1
        return

    for i in range(len(arr)):
        if arr[i] not in newList:
            top = arr[i]
            newList.append(top)
            recur(arr[i+1:], newList, cnt+1)
            newList = newList[:cnt]   # 여기가 약간 핵심. 앞으로 돌아갈 때 몇 번째 자리까지 지워줄 것인지.
    
tempList = []
recur(array, tempList, 0)



# # 내장함수 사용
# from itertools import combinations

# N, M = map(int, input().split())
# array = list(range(1, N+1))

# c = combinations(array, M)
# c = list(c)
# for i in range(len(c)):
#     c[i] = list(c[i])
#     for j in range(len(c[i])):
#         print(c[i][j], end = " ")
#     print()
