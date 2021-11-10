import sys
sys.setrecursionlimit(10**7)
def DFS(y_loc,x_loc):
    if (0 <= x_loc < m) and (0 <= y_loc < n):
        if loc_array[y_loc][x_loc] < 0 or visited[y_loc][x_loc]:
            return
        visited[y_loc][x_loc] = True
        DFS(y_loc + 1,x_loc) #up
        DFS(y_loc - 1,x_loc) #down
        DFS(y_loc,x_loc + 1) #right
        DFS(y_loc,x_loc - 1) #left

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        m,n,k = map(int,sys.stdin.readline().split())
        visited = [[False for _ in range(m+1)] for _ in range(n+1)]
        loc_array = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        baechu = []
        warm_count = 0

        for _ in range(k):
            #x is col, y is row
            x,y = map(int,sys.stdin.readline().split())
            baechu.append((y,x)) # save baechu location 
            loc_array[y][x] = 1

        while baechu: #iterate until all baechu is visited
            y_loc, x_loc = baechu.pop(0)
            if visited[y_loc][x_loc]:
                continue
            warm_count += 1
            DFS(y_loc,x_loc)

        print(warm_count)

    # for v in visited:
    #     print(v)
