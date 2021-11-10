V, E = map(int, input().split())

v_list = [] # (ver1, ver2, len)
for i in range(E):
    a, b, c = map(int, input().split())
    v_list.append((a, b, c))

v_list = sorted(v_list, key = lambda vertex:vertex[2])

sets = []
for i in range(V):
    sets.append([i+1])

res = 0
for vertex in v_list:
    first, second, dist = vertex
    flag = True
    for s in range(len(sets)):
        if first in sets[s] and second in sets[s]:
            flag = False
            continue
        if first in sets[s]:
            first_index = s
        if second in sets[s]:
            second_index = s

    if flag == True:
        sets[first_index] += sets[second_index]
        sets.pop(second_index)
        res += dist

    if len(sets[0]) == V:
        break

print(res)
