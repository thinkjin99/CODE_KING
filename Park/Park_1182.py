# 재귀 사용해서
N, S = map(int, input().split())

array = list(map(int, input().split()))

cnt = 0

def combi(arr, hap):
    global cnt
    if(len(arr)==0):
        return
    for i in range(len(arr)):
        top = arr[i]
        combi(arr[i+1:], hap + top)
        if(hap + top == S):
            cnt+=1
        

combi(array, 0)
print(cnt)


# 재귀 사용 없이
# from itertools import combinations

# N, S = map(int, input().split())

# arr = list(map(int, input().split()))

# cnt = 0

# for i in range(len(arr)):
#     c = combinations(arr, i+1)
#     c = list(c)
#     for j in range(len(c)):
#         if(sum(c[j]) == S):
#             cnt+=1

# print(cnt)