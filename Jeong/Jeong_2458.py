import sys
MAX = 25001
input = sys.stdin.readline
n,m = map(int,input().split())
adj_graph = [[MAX for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    adj_graph[u-1][v-1] = 1

for k in range(n):
    for i in range(n):
        if i == k: continue #사이클이 존재하지 않는 그래프이기에 자신을 경유하는 경우는 continue 해준다.
        for j in range(n):
            if adj_graph[i][k] == 1 and adj_graph[k][j] == 1:
                adj_graph[i][j] = 1
res = 0
for i in range(n):
    is_possible = True
    for j in range(n):
        if adj_graph[i][j] ==  MAX and i != j:
            if adj_graph[j][i] == MAX:
                is_possible = False
                break
    res = res + 1 if is_possible else res
print(res)


    