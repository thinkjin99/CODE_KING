import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
n,k = map(int,input().split())
user_sequence = [int(i) for i in input().split()]
multy_tap = []
product_count = defaultdict(list)
res = 0
for i,u in enumerate(user_sequence): 
    product_count[u].append(i)

in_heap = [False for _ in range(k + 1)]
for u in user_sequence:
    if in_heap[u]: continue #이미 멀티탭에 포함돼 있으면 continue
    #등장 순서가 가장 늦은 원소부터 뽑는다.
    if len(multy_tap) == n:
        _, mul_u = heapq.heappop(multy_tap) # 멀티탭 내부의 가장 늦게 사용하는 전자기기
        in_heap[mul_u] = False #멀티탭에서 뽑아준다.
        print(mul_u)
        res += 1

    in_heap[u] = True #멀티탭에 해당 전자기기를 꽂아준다.
    #최대 힙처럼 사용하기 위해 -1을 곱해준다
    index = -1 * product_count[u].pop(0)
    #만약에 비어있다면, 최대 가중치를 부여한다. 가장 먼저 뽑아야 하므로.
    index = index if product_count[u] else -(k+1) 
    heapq.heappush(multy_tap, (index, u))
print(res)