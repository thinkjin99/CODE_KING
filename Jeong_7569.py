import sys
from collections import deque
# from collections import Counter

def BFS(red_tomatoes):
    queue = deque(red_tomatoes) #따로 반복 처리를 할 필요가 없게 하기 위해
    while queue:
        z,x,y = queue.popleft()
        for dz,dx,dy in [(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]: #현재박스에서 전후좌우
            next_z, next_x, next_y = z + dz, x + dx, y + dy
            if 0 <= next_x < n and 0 <= next_y < m and 0 <= next_z < h and tomatoe_box[next_z][next_x][next_y] == 0: #먼저 도착하는 친구가 최단거리임!!
                    queue.append((next_z,next_x,next_y))
                    tomatoe_box[next_z][next_x][next_y] = tomatoe_box[z][x][y] + 1
        # print('-' * 10)
        # print(queue)
        # for t in tomatoe_box:
        #     for r in t:
        #         print(r)
    

if __name__ == '__main__':
    m,n,h = map(int,input().split())
    red_tomatoes = []
    tomatoe_box = [[[] for _ in range(n)] for _ in range(h)] #3차원 리스트로 토마토 박스를 생성
    green_tomatoes = []
    for height in range(h):
        for row in range(n):
            for col,t in enumerate(map(int,sys.stdin.readline().split())):
                if t == 1: #익은 토마토이면 방문해야 하므로 리스트에 추가
                    red_tomatoes.append((height,row,col))
                if t == 0:
                    green_tomatoes.append((height,row,col)) #익지 않은 토마토의 위치 기억
                tomatoe_box[height][row].append(t)

    if len(green_tomatoes) == 0: #이미 모든 토마토가 익어있음
        print(0)

    else:
        BFS(red_tomatoes)
        res = 0
        for h,r,c in green_tomatoes:
            if tomatoe_box[h][r][c] == 0: #방문하지 못한 토마토가 존재하는 경우
                print(-1)
                sys.exit()  #-1을 출력하고 종료

            res = max(res,tomatoe_box[h][r][c]) #방문한 토마토 중 최대 값을 탐
        print(res - 1)
    

        
        
