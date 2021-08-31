import sys
input = sys.stdin.readline
n,m = map(int,input().split())
    
def bfs(maze):
    visitied = [[0 for _ in range(m)] for _ in range(n)]
    distance = [[float('inf') for _ in range(m)] for _ in range(n)]
    queue = [(0,0)]
    distance[0][0] = 0
    visitied[0][0] = True #시작점은 방문 처리

    while queue:
        cur_y,cur_x = queue.pop(0)
        for dy,dx in zip((-1,1,0,0),(0,0,-1,1)):
            next_y, next_x = cur_y + dy, cur_x + dx
            if 0 <= next_y < n and 0 <= next_x < m and not visitied[next_y][next_x]: #범위 안에 존재하는지 확인
                if maze[next_y][next_x] == '1': continue #벽이면 거리를 초기화 해줄 수 없다.
                distance[next_y][next_x] = distance[cur_y][cur_x] + 1
                queue.append((next_y,next_x))
                visitied[next_y][next_x] = True

    return distance[n-1][m-1]

maze = [[i for i in input().rstrip()] for _ in range(n)]
walls = [(i,j) for i in range(n) for j in range(m) if maze[i][j] == '1'] #벽의 정보 저장
res = float('inf')

while walls:
    cur_wx,cur_wy = walls.pop(0)
    is_potentail_wall = False
    for dy,dx in zip((-1,1,0,0),(0,0,-1,1)): #경로와 이어질 듯한 벽만 허물어준다.
            next_wx, next_wy = cur_wx + dx, cur_wy + dy
            if 0 <= next_wx < n and 0 <= next_wy < m and maze[next_wx][next_wy] == '0':
                is_potentail_wall = True
                break
    
    if is_potentail_wall:
        maze[cur_wx][cur_wy] = '0'
        res = min(res,bfs(maze))
        maze[cur_wx][cur_wy] = '1'

res  = -1 if res == float('inf') else res + 1
print(res)

    



