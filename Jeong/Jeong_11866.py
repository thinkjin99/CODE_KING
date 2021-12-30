import sys
from collections import deque
input = sys.stdin.readline
n, k  = map(int, input().split())
ans = []
q = deque([str(i) for i in range(1, n + 1)])
while q:
    for _ in range(k - 1):
        deque.rotate(q, -1)
    ans.append(deque.popleft(q))
print(f"<{', '.join(ans)}>")