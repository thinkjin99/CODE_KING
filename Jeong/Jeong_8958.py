n = int(input())
cases = [input() for _ in range(n)]
ans = []
for case in cases:
    count = 0
    res = 0
    for s in case:
        if s == 'O':
            count += 1
            res += count
        else: count = 0
    ans.append(res)
for a in ans:
    print(a)
