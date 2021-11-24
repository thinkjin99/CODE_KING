import sys
from collections import deque
input = sys.stdin.readline
h_queue = deque([0] * 4)
v_queue = deque([0] * 4)
n, m, x, y, cmd_num = map(int,input().split())
_map = [[int(i) for i in input().split()] for _ in range(n)]
command = [int(i) for i in input().split()]
direction = [(0,1),(0,-1),(-1,0),(1,0)]
def change_under(queue, _map, x, y):
    if _map[x][y] == 0:
        _map[x][y] = queue[-1]
    else: 
        queue[-1] = _map[x][y]
        _map[x][y] = 0
    return

for c in command:
    dx, dy = direction[c-1]
    next_x, next_y = x + dx, y + dy
    if 0 <= next_x < n and 0 <= next_y < m:
        if c >= 3:
            if c == 3:
                v_queue.rotate(1)
            elif c == 4:
                v_queue.rotate(-1)
            change_under(v_queue, _map, next_x, next_y)
            h_queue[1], h_queue[-1] = v_queue[1], v_queue[-1]
        else:
            if c == 1:
                h_queue.rotate(1)
            elif c == 2:
                h_queue.rotate(-1)
            change_under(h_queue, _map, next_x, next_y)
            v_queue[1],v_queue[-1] = h_queue[1],h_queue[-1]
        x += dx; y += dy;
        print(h_queue[1])
