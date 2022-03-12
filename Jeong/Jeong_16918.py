r,c,n = map(int, input().split())
boom_map = [list(input()) for _ in range(r)]

def find_boom(boom_list):
    for y in range(r):
        for x in range(c):
            if boom_map[y][x] == 'O':
                boom_list.append((y, x))
    return boom_list

def set_boom():
    boom_map = [['O' for _ in range(c)] for _ in range(r)]
    return boom_map

def explosion(boom_list, boom_map):
    while boom_list:
        y, x = boom_list.pop()
        boom_map[y][x] = '.'
        for dy,dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            ny, nx = y + dy, x + dx
            if (0 <= ny < r) and (0 <= nx < c):
                boom_map[ny][nx] = '.'

n -= 1
while n:
    boom_list = find_boom([])
    boom_map = set_boom()
    n -= 1
    if n == 0:
        break
    n -= 1
    explosion(boom_list, boom_map)

for b in boom_map:
    print(''.join(b))


