N = int(input())

# 입력과 동시에 배열에 숫자 넣기
arr = [list(map(int, input().split())) for i in range(N)]

v_list = [] # (ver1, ver2, len)
for i in range(N):
    for j in range(i):
        v_list.append((i+1, j+1, arr[i][j]))

# 거리 기준으로 정렬
v_list = sorted(v_list, key = lambda vertex:vertex[2])

# 집합? 형태로 저장해둘 배열
sets = []
for i in range(N):
    sets.append({i+1})

# v_list 돌면서 연결되어있는 두 노드가 같은 위치의 집합에 있는지 확인
res = 0
for vertex in v_list:
    first, second, dist = vertex
    flag = True
    first_index = None
    second_index = None
    for s in range(len(sets)):
        # 각각의 위치 기록해줌
        if first in sets[s]:
            first_index = s
        if second in sets[s]:
            second_index = s  

        # 같은 위치에 있으면 그냥 넘기고 (순환?되면 안되니깐!)
        if(first_index != None and first_index == second_index):
            flag = False
            break

    # 각 노드가 들어가있던 거 하나로 합쳐주기
    if flag == True:
        sets[first_index] = sets[first_index].union(sets[second_index])
        sets.pop(second_index)
        res += dist

    # 모든 노드들이 하나의 배열에 다 들어가있따면 종료
    if len(sets[0]) == N:
        break

print(res)
