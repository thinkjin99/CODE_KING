import sys
# from collections import Counter

def BFS(tomatoe_loc):
    queue = set() #따로 반복 처리를 할 필요가 없게 하기 위해
    x,y = tomatoe_loc
    queue.add((x,y,0))
    days_map[x][y] = 0

    while queue:
        x,y,days = queue.pop()
        for dx,dy in zip((0, 1, 0, -1),(1, 0, -1, 0)): #현재박스에서 상하좌우
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < n and 0 <= next_y < m:
                if tomatoe_box[next_x][next_y] == 0 and days + 1 < days_map[next_x][next_y]:
                    queue.add((next_x, next_y, days + 1))
                    days_map[next_x][next_y] = days + 1


if __name__ == '__main__':
    m,n,h = map(int,input().split())
    tomatoes = []
    tomatoe_box = [[] for _ in range(n)]
    days_map = [[100 for _ in range(m)] for _ in range(n)] #각 토마토까지 익는데 걸리는 날짜를 저장한다.
    for row in range(n):
        for col,t in enumerate(map(int,sys.stdin.readline().split())):
            if t == 1: #익은 토마토이면 방문해야 하므로 리스트에 추가
                tomatoes.append((row,col))
            tomatoe_box[row].append(t)

    if len(tomatoes) == sum([len(b) for b in tomatoe_box]): #이미 모든 토마토가 익어있음
        print(0)

    else:
        for t in tomatoes:
            BFS(t)

        unreachable = sum([d.count(100) for d in days_map])
        empy_count = sum([b.count(-1) for b in tomatoe_box])

        if empy_count <= unreachable:
            print(-1)  #익지 않는 토마토가 존재

        else:
            print(days_map)