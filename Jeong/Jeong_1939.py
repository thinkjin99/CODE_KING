import sys
input = sys.stdin.readline
n,m = map(int,input().split())
bridges = [[] for _ in range(n + 1)]
weights = []
for _ in range(m):
    u,v,w = map(int,input().split())
    bridges[u].append((v,w))
    bridges[v].append((u,w))
    weights.append(w)

start,end = map(int,input().split())
def check_bridge(queue, dest, weight):
    visited = [False] * (n + 1)
    while queue:
        if visited[dest]:
            return True
        current = queue.pop()
        for v, bridge_capa in bridges[current]:
            if bridge_capa >= weight and not visited[v]:
                queue.append(v)
                visited[v] = True
    return False

left = 0; right = len(weights) - 1
max_weight = 0
weights.sort()
while left <= right:
    mid = (left + right) // 2
    if check_bridge([start], end, weights[mid]):
        max_weight = weights[mid]
        left = mid + 1
    else:
        right = mid - 1
print(max_weight)
