import sys
def bfs():
    answer = 1
    queue = set() #따로 반복 처리를 할 필요가 없게 하기 위해
    queue.add((0, 0, 1, board[0][0]))
 
    while queue:
        x, y, cnt, sentence = queue.pop()
        answer = max(answer, cnt)
        for dx,dy in zip((0, 1, 0, -1),(1, 0, -1, 0)): #상하좌우
            next_x, nexty = x + dx, y + dy
            if 0 <= next_x < r and 0 <= nexty < c:
                if board[next_x][nexty] not in sentence:
                    queue.add((next_x, nexty, cnt + 1, sentence + board[next_x][nexty]))
    return answer

r, c = map(int, input().split())
board = [sys.stdin.readline().rstrip() for _ in range(r)]
print(bfs())