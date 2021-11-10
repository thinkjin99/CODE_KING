import heapq
import sys
N = int(input())
h = [int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(h)
minDeck = heapq.heappop(h)
ans = 0
while len(h) > 0:
    cards = heapq.heappop(h) #현재 큐에 존재하는 최소 값
    heapq.heappush(h,minDeck + cards) #지금까지의 최소 카드 뭉치에 현재의 최소 카드 수를 더 해준뒤 큐에 넣어준다.
    ans += minDeck + cards #최소 카드 뭉치에 카드를 더해준다.
    minDeck = heapq.heappop(h) #새로운 뭉치를 추가한 뒤 최소 값을 추출 해준다.
print(ans)