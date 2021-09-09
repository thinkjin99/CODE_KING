#https://summa-cum-laude.tistory.com/35
import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
heap = [(-arr[0][0],0,0)] #가장 높이가 높은 요소부터 추출해야하기 때문에 heap 사용
while heap:
    num, cur_y, cur_x = heapq.heappop(heap)
    for y,x in zip((0,0,1,-1),(-1,1,0,0)):
        next_y,next_x = (cur_y + y, cur_x + x)
        if 0 <= next_y < n and 0 <= next_x < m:
            if -num > arr[next_y][next_x]: #최대힙과 같이 작동해야 하므로 -를 붙여준다.
                if not dp[next_y][next_x]: #dp배열이 초기화 되어 있지 않다면, 방문하지 않은 것이므로 push
                    heapq.heappush(heap,(-arr[next_y][next_x],next_y,next_x))
                dp[next_y][next_x] += dp[cur_y][cur_x]
print(dp[n-1][m-1])
