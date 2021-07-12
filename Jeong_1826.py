import heapq
import sys
n = int(sys.stdin.readline()) + 1
info = []
for _ in range(n):
   loc,oil = map(int,sys.stdin.readline().rstrip().split())
   info.append((loc,oil))
town,nowOil = info.pop()
maxHeap = []
info.sort()
index,ans = (0,0)
while nowOil < town:
    for loc,oil in info[index:]:
        if loc > nowOil: break #현재 기름량으로 도착할 수 있는 주요소라면.
        heapq.heappush(maxHeap,-oil)
        index += 1
    if len(maxHeap) == 0:
        ans = -1
        break
    nowOil -= heapq.heappop(maxHeap)

    ans += 1
print(ans)
