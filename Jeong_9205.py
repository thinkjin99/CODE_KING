import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input()) + 2
    graph = [[0 for _ in range(n)] for _ in range(n)]
    nodes = [tuple(map(int,input().split())) for _ in range(n)]
    for row,(i_x, i_y) in enumerate(nodes):
        for col,(j_x, j_y) in enumerate(nodes):
            if i_x == j_x and i_y == j_y: continue #자기 자신인 경우 continue
            if abs(i_x - j_x) + abs(i_y - j_y) <= 1000:
                graph[row][col] = 1

    for k in range(n):
        for i in range(n):
            if k == i: continue
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    res = 'happy' if graph[0][-1] else 'sad'
    print(res)

