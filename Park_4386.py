def dist(x1, y1, x2, y2):
    return round(((x1-x2)**2 + (y1-y2)**2)**(1/2), 2)

N = int(input())
arr = [[float("inf") * i for i in range(N)] for j in range(N)]

input_arr = []
for i in range(N):
    a, b = map(float, input().split())
    input_arr.append([a,b])

final_arr = []
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        else:
            a, b = input_arr[i]
            c, d = input_arr[j]
            final_arr.append((i, j, dist(a, b, c, d)))

final_arr = sorted(final_arr, key=lambda vertex:vertex[2])
sets = []
for i in range(N):
    sets.append({i})

ret = 0
for i in final_arr:
    ver1, ver2, dist = i
    ver1_idx = 0
    ver2_idx = 0
    for j in sets: 
        if ver1 in j:
            ver1_idx = sets.index(j)
        if ver2 in j:
            ver2_idx = sets.index(j)

    if ver1_idx == ver2_idx:
        continue
    else:
        ret += dist
        sets[ver1_idx] = sets[ver1_idx].union(sets[ver2_idx])
        sets.pop(ver2_idx)

print(ret)
            
