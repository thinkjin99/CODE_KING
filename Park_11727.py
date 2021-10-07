N = int(input())

res = [1, 3]
for i in range(2, N):
    res.append(res[i-1]+res[i-2]*2)

print(res[N-1]%10007)
