from re import I
import sys
from collections import deque
N = int(input().rstrip())
shark_map = [[int(i) for i in input().split()] for _ in range(N)]
fish_map = [[0] * N] * N
fish_cnt = 0
size = 2
def bfs(shark_size, shark_r, shark_c):
    directions = list(zip([0,-1,0,1],[-1,0,1,0])) #lsit로 변환안하면 반복문이 실행이 안됨??
    queue = deque([(shark_r, shark_c)])
    while queue:
        cur_r, cur_c = queue.popleft()
        print(cur_r,cur_c)
        # if (shark_map[cur_r][cur_c] > 0) and (shark_map[cur_r][cur_c] < shark_size):
        #     global fish_cnt
        #     fish_cnt += fish_map[cur_r][cur_c]
        #     if fish_cnt == shark_size:
        #         shark_size += 1
        #         fish_cnt = 0
        #     return (shark_size, cur_r, cur_c)
        # shark_map[cur_r][cur_c] = 999
        for dr,dc in directions:
            nr,nc = cur_r + dr, cur_c + dc
            print(cur_r,cur_c)
            # if (0 <= nr < N) and (0 <= nc < N):
                # if shark_map[nr][nc] <= shark_size:
            queue.append((nr,nc))
    return

for i in range(N):
    for j in range(N):
        if shark_map[i][j] == 9:
            now_r = i
            now_c = j
            break
time = 0
bfs(2,now_r,now_c)
# while True:
#     before_r, before_c = now_r, now_c
#     res = bfs(size,now_r,now_c)
#     print(res)
#     if res:
#         size, now_r, now_c = res
#     else: break
#     time += abs(before_r - now_r) + abs(before_c - now_c)

# for f in fish_map:
#     print(f)



