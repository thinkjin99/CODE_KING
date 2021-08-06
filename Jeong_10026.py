import sys
# def check_close_color(color_map):
#     for x in range(n):
#         for y in range(n):
#             is_closed_color = set()
#             for dx,dy in zip((1,-1,0,0),(0,0,-1,1)):
#                 next_x,next_y = x + dx, y + dy
#                 if (0 <= next_x < n) and (0 <= next_y < n):
#                     closed_color = color_map[next_x][next_y]
#                     is_closed_color.add(closed_color)
            
#             if len(is_closed_color) == 1:
#                 color_map[x][y] = closed_color

def BFS():
    queue = set() #따로 반복 처리를 할 필요가 없게 하기 위해
    queue.add()
 
    while queue:
        x, y, cnt, sentence = queue.pop()
        answer = max(answer, cnt)
        for dx,dy in zip((0, 1, 0, -1),(1, 0, -1, 0)): #상하좌우
            next_x, nexty = x + dx, y + dy
            if 0 <= next_x < r and 0 <= nexty < c:
                if board[next_x][nexty] not in sentence:
                    queue.add((next_x, nexty, cnt + 1, sentence + board[next_x][nexty]))
    return answer


if __name__ == '__main__':
    n = int(input())
    color_map = [[] for _ in range(n)]
    for i in range(n):
        for c in sys.stdin.readline().rstrip():
            color_map[i].append(c)
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r in color_map:
        print(r)