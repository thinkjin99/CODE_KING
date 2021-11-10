N = int(input())
K = int(input())

# 아무것도 없는 건 0
board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1 # 사과 위치를 1

L = int(input())
rot_list = []
for _ in range(L):
    temp = input()
    a, b = temp.split()
    rot_list.append((int(a), b)) # 초, 방향

time = 1
ch_time, ch_direct = rot_list.pop(0)

# 현재 움직이는 방향... 오른쪽부터 시계방향으로 0123
mv_direct = 0

# 움직이는 방향... 방법? 지정
move_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상

# 현재 좌표
x = 0
y = 1

# 뱀이 board에 닿아있는 위치 저장 list
snake_list = [(0, 0)]

while True:
    # 벽이랑 충돌 검사
    if x >= N or y >= N:
        break
    if x < 0 or y < 0:
        break

    # 뱀 대가리가 자기 스스로한테 부딪혔을 때
    if (x, y) in snake_list:
        break

    snake_list.append((x, y))

    if board[x][y] == 1:
        board[x][y] = 0
    elif board[x][y] == 0:
        snake_list.pop(0)


    # 방향 전환
    if time == ch_time:
        if ch_direct == 'L' and mv_direct == 0:
            mv_direct = 3
        elif ch_direct == 'L' and mv_direct != 0:
            mv_direct -= 1
        elif ch_direct == 'D' and mv_direct == 3:
            mv_direct = 0
        else:
            mv_direct += 1
        
        try:
            ch_time, ch_direct = rot_list.pop(0)
        except:
            pass

    x = x + move_list[mv_direct][0]
    y = y + move_list[mv_direct][1]
    
    time += 1


print(time)        
