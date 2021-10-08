import sys
input = sys.stdin.readline
N,M = map(int,input().split())
cheese = [[int(i) for i in input().split()] for _ in range(N)]
cheese_row = [[] for _ in range(N)]
cheese_col = [[] for _ in range(M)]
for i in range(N):
    for j in range(M):
        if cheese[i][j]:
            cheese_row[i].append(j)
            cheese_col[j].append(i)
res = 0
while sum(map(len,cheese_row)):
    cheese_to_melt = []
    for r in range(1,N):
        for c in range(1,M):
            if not cheese[r][c]: continue
            empty = []
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = r + dr; nc = c + dc
                if 0 <= nr < N and 0 <= nc < M:   
                    if cheese[nr][nc] == 0:
                        empty.append((nr,nc))
            closed_empty = 0
            for row,col in empty:
                if cheese_row[row] and cheese_col[col]:
                    if cheese_row[row][0] < c < cheese_row[row][-1] and cheese_col[col][0] < r < cheese_col[col][-1]:
                        closed_empty += 1

            if len(empty) - closed_empty >= 2:
                cheese_to_melt.append((r,c))
                if cheese_row[r]:
                    cheese_row[r].remove(c)
                if cheese_col[c]:
                    cheese_col[c].remove(r)

    for mr,mc in cheese_to_melt:
        cheese[mr][mc] = 0

    for c in cheese:
        print(c)
    print('\n\n\n')
    res += 1
print(res)

