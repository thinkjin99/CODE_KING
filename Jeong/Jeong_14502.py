n,m = map(int, input().split())
cur_x, cur_y, dir_index = map(int, input().split())
clean_map = [[int(i) for i in input().split()] for _ in range(n)]
directions = [(-1,0),(0,1),(1,0),(0,-1)] #n,e,s,w
total_cnt = 0
def dfs(clean_map, dir_index, current):
    cur_x, cur_y = current
    if clean_map[cur_x][cur_y] == 0:
        clean_map[cur_x][cur_y] = 2 #청소는 2
        global total_cnt
        total_cnt += 1

    for i in range(4):
        next_dir_index = (dir_index + 3 - i) % 4
        dx, dy = directions[next_dir_index]
        next_x, next_y = cur_x + dx, cur_y + dy
        if (0 < next_x < n) and (0 < next_y < m):
            if clean_map[next_x][next_y] == 0:
                dfs(clean_map, next_dir_index,(next_x, next_y))

    dx, dy = directions[(dir_index + 2) % 4]
    next_x, next_y = cur_x + dx, cur_y + dy
    if (0 <= next_x <= n) and (0 <= next_y <= m): #벽을 검사해야 하기 때문에 0과 N인 경우를 포함해 확인해야한다.
        if clean_map[next_x][next_y] == 1: #1칸 후진했을 때 
            print(total_cnt)
            exit(0) #후진하는 순간 끝나야 한다.
        dfs(clean_map,dir_index,(next_x,next_y))

dfs(clean_map,dir_index,(cur_x, cur_y))
