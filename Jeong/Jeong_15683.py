import sys
input = sys.stdin.readline
n,m = map(int, input().split())
ans = 0
def cctv_direction(cctv_type):
    if cctv_type == 1:
        cctv_direction = [[(0,1)],[(0,-1)],[(1,0)],[(-1,0)]]
    if cctv_type == 2:
        cctv_direction = [[(1,0),(-1,0)],[(0,1),(0,-1)]]
    if cctv_type == 3:
        cctv_direction = [[(0,1),(1,0)],[(0,1),(-1,0)],[(0,-1),(1,0)],[(0,-1),(-1,0)]]
    if cctv_type == 4:
        #0,-1 , 1,0 , 0,1 ,- 1,0
        cctv_direction = [[(0,1),(1,0),(-1,0)],[(0,1),(-1,0),(0,-1)],[(0,-1),(1,0),(-1,0)],[(0,-1),(0,1),(1,0)]]
    if cctv_type == 5:
        cctv_direction = [[(0,1),(0,-1),(1,0),(-1,0)]]
    return cctv_direction

def brute(cctvs, cctv_map, counts):
    if not cctvs:
        global ans
        ans = max(ans,counts)
        return counts
    cctv_x, cctv_y, cctv_type = cctvs.pop(0)
    valid_directons = cctv_direction(cctv_type)
    for directions in valid_directons:
        visited = []
        cur_count = 0
        for dx, dy in directions:
            next_x,next_y = cctv_x + dx, cctv_y + dy
            while(0 <= next_x < n and 0 <= next_y < m):
                if cctv_map[next_x][next_y] == 0:
                    cctv_map[next_x][next_y] = -1
                    cur_count += 1
                    visited.append((next_x, next_y)) #변경한 값을 원상 복귀 하기 위해 사용한다.
                elif cctv_map[next_x][next_y] == 6:
                    break
                next_x += dx; next_y += dy
        brute(cctvs[:], cctv_map, counts + cur_count)
        for x,y in visited:
            cctv_map[x][y] = 0
    return
    
if __name__ == '__main__':
    cctv_map = [[0 for _ in range(m)] for _ in range(n)]
    cctvs = []
    block_num = 0
    for i in range(n):
        for j,v in enumerate(input().split()):
            v = int(v)
            cctv_map[i][j] = v
            if 0 < v < 6:
                cctvs.append((i,j,v))
            elif v == 6:
                block_num += 1
    cctv_count = len(cctvs)
    brute(cctvs, cctv_map, 0)
    print(m * n - (cctv_count + ans + block_num))
