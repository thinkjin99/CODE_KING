import sys
import heapq
N = int(input())
h = [0 for _ in range(N)]
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for i in row:
        if h[0] < i:
            heapq.heapreplace(h,i)
print(heapq.heappop(h))
