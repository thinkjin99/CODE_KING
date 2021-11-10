import sys
from collections import deque

def BFS(x_,y_,visited):
    queue = deque() #따로 반복 처리를 할 필요가 없게 하기 위해
    queue.append((x_,y_))
    while queue:
        x, y = queue.pop()
        for dx,dy in zip((0, 0, -1, 1),(1, -1, 0, 0)): #상하좌우
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < n and 0 <= next_y < n) and not visited[next_x][next_y]:
                if color_map[x_][y_] == color_map[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
def do_BFS():
    area_count = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                BFS(r,c,visited)
                area_count += 1
    return area_count

if __name__ == '__main__':
    n = int(input())
    color_map = [[] for _ in range(n)]
    red_loc = [] #빨간색이 저장된 위치를 저장한다.
    for r in range(n):
        for col_index,color in enumerate(sys.stdin.readline().rstrip()):
            color_map[r].append(color)
            if color == 'R':
                red_loc.append((r,col_index))

    noraml = do_BFS()
    
    for r,c in red_loc: #빨간색을 전부 초록색으로 변환
        color_map[r][c] = 'G'
    
    color_blind = do_BFS()

    print(noraml,color_blind)