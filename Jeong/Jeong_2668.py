import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input().rstrip()) for _ in range(1, n + 1)]
res = [False] * n
for i,v in enumerate(nums,start=1):
    index = i - 1
    visited = [False] * n
    while visited[index] == False: #사이클 시작
        visited[index] = True
        index = nums[index] - 1
    if index == i - 1: #사이클이 존재하는 경우 저장
        res = [r | v for r,v in zip(res, visited)]

print(sum(res))
for i,r in enumerate(res,start=1):
    if r:
        print(i)