import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
shark_map = [[int(i) for i in input().split()] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if shark_map[i][j] == 9:
            shark_r = i
            shark_c = j
            shark_map[i][j] = 0
            break

def bfs(shark_r, shark_c):
    queue = deque([(shark_r, shark_c, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[shark_r][shark_c] = True
    edible_fish = [] #먹을 수 있는 물고기들
    min_edible_dist = int(1e9) #먹을 수 있는 물고기까지의 최소거리
    while queue:
        cur_r, cur_c, distance = queue.popleft()
        for dr,dc in directions:
            nr,nc = cur_r + dr, cur_c + dc
            if (0 <= nr < N) and (0 <= nc < N) and (not visited[nr][nc]):
                if (shark_map[nr][nc] <= shark_size):
                    visited[nr][nc] = True 
                    next_distance = distance + 1
                    if (0 < shark_map[nr][nc] < shark_size):
                        min_edible_dist = distance
                        edible_fish.append((next_distance, nr, nc))
                    if next_distance <= min_edible_dist: #거리가 더 멀어지면 탐색할 필요가 없다.
                        queue.append((nr,nc,next_distance))
    if edible_fish:
        edible_fish.sort() #거리, 행 순으로 정렬 된다.
        return edible_fish[0]
    else: return

time = 0
eat_fish_cnt = 0
shark_size = 2
directions = list(zip([-1,0,0,1],[0,-1,1,0]))
while True:
    before_r, before_c = shark_r, shark_c
    res = bfs(shark_r, shark_c)
    if res:
        dist, shark_r, shark_c = res
        time += dist
        eat_fish_cnt += 1
        if eat_fish_cnt == shark_size:
            eat_fish_cnt = 0
            shark_size += 1
        shark_map[shark_r][shark_c] = 0 #상어의 위치를 0으로 업데이트
    else: break #먹을 수 있는 물고기가 더 존재하지 않으면 종료
print(time)