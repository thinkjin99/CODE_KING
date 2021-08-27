from heapq import heappush, heappop

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    heapList = []
    for num in arr:
        heappush(heapList, num)

    res = 0
    while len(heapList) != 1:
        a = heappop(heapList)
        b = heappop(heapList)
        heappush(heapList, a+b)
        res += a+b

    print(res)

    
