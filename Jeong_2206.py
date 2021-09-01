import sys
input = sys.stdin.readline
n,m = map(int,input().split())
    
def bfs(maze):
    distance = [[[0,0] for _ in range(m)] for _ in range(n)] #벽을 부신 경우 부수지 않은 경우로 나눠 선언한다.(n,m,2)
    queue = [(0,0,0)]
    distance[0][0][0] = 1

    while queue:
        cur_y,cur_x,cur_w = queue.pop(0)
        if cur_y == n - 1 and cur_x ==  m - 1: 
                return distance[cur_y][cur_x][cur_w]
        
        for dy,dx in zip((-1,1,0,0),(0,0,-1,1)):
            next_y, next_x = cur_y + dy, cur_x + dx
            #범위 안에 존재하는지 확인, 처음 방문한 요소가 최소 거리이기 때문에 distance가 초기화 돼 있다면 다시 초기화 할 필요 없다. 
            if 0 <= next_y < n and 0 <= next_x < m and not distance[next_y][next_x][cur_w]: 
                if maze[next_y][next_x] == '0':
                    #벽이 없는 경우 벽을 부수지 않는 distance를 초기화 해준다.
                    distance[next_y][next_x][cur_w] = distance[cur_y][cur_x][cur_w] + 1
                    queue.append((next_y,next_x,cur_w))
                if maze[next_y][next_x] == '1' and cur_w == 0: #처음으로 벽을 부수는 경우
                    #벽이 있는 경우 처음으로 벽을 부쉈다면, 벽을 부순 distance를 초기화 한다.
                    distance[next_y][next_x][1] = distance[cur_y][cur_x][cur_w] + 1
                    queue.append((next_y,next_x,1))

    return -1

maze = [[i for i in input().rstrip()] for _ in range(n)]
res = bfs(maze)
print(res)

    



