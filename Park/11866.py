from collections import deque

n, k = map(int, input().split())

arr = deque([i for i in range(1, n+1)])

print("<", end="")

while len(arr)>1:
    for i in range(k):
        arr.rotate(-1)  # 원형 큐 회전
    print(arr.pop(), end=", ")

print(arr.pop(), end=">")
