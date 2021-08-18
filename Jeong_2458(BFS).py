from collections import deque
import sys
MAX = 25001
input = sys.stdin.readline
n,m = map(int,input().split())
adj_graph = [[MAX for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    adj_graph[u-1][v-1] = 1

def bfs(start):
    queue = deque([start])
    visited = [False for _ in range(n)]
    while queue:
        u = queue.popleft()
        for i,v in enumerate(adj_graph[u]):
            if not visited[i] and v != MAX:
                queue.append(i)
                visited[i] = True
    
    for i,v_ in enumerate(visited): #방문 가능한 점이라면 경로가 존재하는 것이므로
        if v_:
            adj_graph[start][i] = 1

for i in range(n): #각 row에 대해 방문 탐색을 진행한다.
    bfs(i)

res = 0
for i in range(n):
    is_possible = True
    for j in range(n):
        if adj_graph[i][j] ==  MAX and i != j: #자기 자신으로의 경로는 존재하지 않으므로
            if adj_graph[j][i] == MAX: 
                #경로가 없다는 것은 나와 완전히 관계 없는 노드이거나 큰 노드인 경우이다.
                #관계가 없다면 키 비교가 불가능하므로 자신 보다 큰 노드인지 여부를 확인해준다.
                is_possible = False #관계가 없다면 순서를 알 수 없다.
                break
    res = res + 1 if is_possible else res #모든 노드와 관계가 존재한다면 순서를 알 수 있다.
print(res)


    