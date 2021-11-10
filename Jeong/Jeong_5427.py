import sys
input = sys.stdin.readline
#이게 한 바퀴 실행 될 때마다 1초가 지난다.
def check_possible_way(building_map, check_queue, is_person = False):
    fire_queue = []; person_queue = []
    while check_queue:
        cur_x, cur_y = check_queue.pop() #현재의 위치
        cur_v = building_map[cur_x][cur_y]
        for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]: #좌표 평면과 달리 x가 세로임
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < h and 0 <= next_y < w:
                next_v = building_map[next_x][next_y]
                #길이면 번지거나 이동 할 수 있다.
                if next_v != '*' and next_v != '#':
                    #사람이 갈 수 있는 길을 탐색하는 경우 중복을 방지하기 위해 값이 적은 경우만 큐에 넣어준다.
                    if is_person and cur_v != '*':
                        if (next_v > cur_v + 1): 
                            person_queue.append((next_x, next_y))
                            building_map[next_x][next_y] = cur_v + 1
                    else: #불이 번지는 것을 구하는 중이면 불을 넣어준다.
                        building_map[next_x][next_y] = '*'
                        fire_queue.append((next_x, next_y))
            else: #끝자리에 요소한 원소가 정수이면 -> 길이 존재한다.
                if cur_v != '*': return cur_v
    if is_person: return person_queue
    else: return fire_queue

for _ in range(int(input())):
    w,h = map(int,input().split())
    building_map = [['#' for _ in range(w)] for _ in range(h)]
    fire_queue = []
    person_queue = []
    is_impossible = True
    for r in range(h):
        for c, j in enumerate(input()):
            if j == '.': 
                building_map[r][c] = float('inf')
            elif j == '*':
                building_map[r][c] = '*'
                fire_queue.append((r,c))
            elif j == '@':
                building_map[r][c] = 0
                person_queue.append((r,c))

    while person_queue or fire_queue:
        person_queue = check_possible_way(building_map, person_queue, is_person=True)
        if isinstance(person_queue,int): #int형 자료형인지 확인
            is_impossible = False 
            print(person_queue + 1)
            break
        fire_queue = check_possible_way(building_map, fire_queue, is_person=False) #불을 먼저 업데이트 해준다.
    if is_impossible:
        print("IMPOSSIBLE")