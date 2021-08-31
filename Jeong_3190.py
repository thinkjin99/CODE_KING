import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
apples = [tuple(map(int,input().split())) for _ in range(int(input()))]
command = [tuple(input().split()) for _ in range(int(input()))]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
visited = [[False for _  in  range(n+1)] for _ in range(n + 1)] #몸 충돌 검사 배열
snake = deque()
snake.append((1,1))
time,cur_direction = 0, 0
while True:
    if len(command) != 0 and time == int(command[0][0]): #시간과 방향전환 확인
        _, direction = command.pop(0)
        if direction == 'D':
            cur_direction += 1 #오른쪽이면 방향 커맨드에서 +1
        else:
            cur_direction -= 1
        cur_direction %= 4 #방향 배열의 범위에서 벗어나면 안됨으로
    
    next_r =  snake[0][0] + directions[cur_direction][0]
    next_c =  snake[0][1] + directions[cur_direction][1]
    time += 1

    if 1 <= next_r <= n and 1 <= next_c <= n and not visited[next_r][next_c]:
        snake.appendleft((next_r,next_c))
        visited[next_r][next_c] = True
        l_apple = len(apples) #기존 사과의 길이
        apples = list(filter(lambda apple: apple[0] != next_r or apple[1] != next_c,apples)) #지나온 사과는 제거해준다.
        if len(apples) != l_apple: continue  #사과가 존재하는 경우 몸의 크기가 늘어나므로 pop할 필요 없다.
        tail_r,tail_c = snake.pop() #몸이 다 빠져나왔으므로 다시 방문할 수 있다.
        visited[tail_r][tail_c] = False

    else:
        break

print(time)

