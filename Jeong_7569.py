import sys
# from collections import Counter

def BFS(tomato_loc):
    queue = set() #따로 반복 처리를 할 필요가 없게 하기 위해
    z,x,y = tomato_loc
    queue.add((z,x,y,0))
    date_map[z][x][y] = 0 #시작위치는 도달까지 0일이 걸림으로

    while queue:
        z,x,y,days = queue.pop()
        for dx,dy in zip((0, 1, 0, -1),(1, 0, -1, 0)): #현재박스에서 전후좌우
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < n and 0 <= next_y < m:
                if tomatoe_box[z][next_x][next_y] == 0 and days + 1 < date_map[z][next_x][next_y]:
                    queue.add((z,next_x, next_y, days + 1))
                    date_map[z][next_x][next_y] = days + 1

        for dz in (1,-1): #현재 위치의 상,하에 인접한 토마토 검사
            next_z = z + dz
            if 0 <= next_z < h:
                if tomatoe_box[next_z][x][y] == 0 and days + 1 < date_map[next_z][x][y]:
                    queue.add((next_z,x, y, days + 1))
                    date_map[next_z][x][y] = days + 1



if __name__ == '__main__':
    m,n,h = map(int,input().split())
    red_tomatoes = []
    tomatoe_box = [[[] for _ in range(n)] for _ in range(h)] #3차원 리스트로 토마토 박스를 생성
    date_map = [[[100 for _ in range(m)] for _ in range(n)] for _ in range(h)] #각 토마토까지 익는데 걸리는 날짜를 저장한다.
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
        for tomato_loc in red_tomatoes:
            BFS(tomato_loc)
        
        res = 0
        for h,r,c in green_tomatoes:
            if date_map[h][r][c] == 100: #방문하지 못한 토마토가 존재하는 경우
                print(-1)
                break  #-1을 출력하고 종료
            else:
                res = max(res,date_map[h][r][c]) #방문한 토마토 중 최대 값을 탐색
        
        print(res)
    

        
        
