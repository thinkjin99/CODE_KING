N = int(input())
M = int(input())

arr = [list(map(int, input().split())) for i in range(M)]

arr = sorted(arr, key = lambda vertex:vertex[2])

sets = []
for i in range(N):
    sets.append({i})  # 여기서 0부터 N-1까지 넣어줬으니깐

total = 0
for i in range(len(arr)):
    verA, verB, dist = arr[i]
    a_idx=0
    b_idx=0
    for one in sets:
      # 여기서 비교할 땐 vertex-1로 해야됨
        if verA-1 in one:
            a_idx = sets.index(one)
        if verB-1 in one:
            b_idx = sets.index(one)

    if a_idx == b_idx:
        continue
    else:
        total += dist
        sets[a_idx] = sets[a_idx].union(sets[b_idx])
        sets.pop(b_idx)

    if len(sets) == N:
        break

print(total)
