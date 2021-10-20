from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
cheese = [[int(i) for i in input().split()] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
res = 0
def BFS(start_points):
    q = deque()
    for x,y in start_points:
        q.append((x,y))

    cheese_to_check = set()
    while q:
        cur_r, cur_c = q.pop()
        for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr = cur_r + dr; nc = cur_c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not cheese[nr][nc] and not visit[nr][nc]: #빈 공간이면 큐에 추가해준다.
                    q.append((nr,nc))
                    visit[nr][nc] = 1

                elif cheese[nr][nc]: #빈공간이 아니라 치즈라면 녹일지 말지를 확인해줘야 한다.
                    cheese_to_check.add((nr,nc))    

    return cheese_to_check #확인해야할 치즈들 

cheese_to_check = BFS([(1,1)])

cnt = 0
while cheese_to_check: #검사할 치즈의 수만큼 반복한다.
    cheese_to_remove = []
    for r,c in cheese_to_check:
        empty_count = 0
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr = r + dr; nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:   
                if visit[nr][nc]: #방문 했다면 해당 부분은 빈공간이다.
                    empty_count += 1

        if empty_count >= 2: #빈공간의 수가 2 이상이면 녹여야 한다.
            cheese_to_remove.append((r,c))

    for cr,cc in cheese_to_remove: #녹일 치즈를 녹이고 방문처리 해준다.
        cheese[cr][cc] = 0
        visit[cr][cc] = 1

    cheese_to_check = BFS(cheese_to_remove) #삭제된 치즈의 위치를 큐에 업데이트 해주고 BFS 탐색한다.
    cnt += 1

print(cnt)
    # for v in visit:
    #     print(v)
    # print('\n\n\n')
    # for c in cheese:
    #     print(c)
    # print('\n\n\n')

