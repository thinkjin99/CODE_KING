n = int(input())
pole = {}
for _ in range(n):
    key, value = map(int,input().split())
    pole[key] = value
length = [1] * n
lines = [pole[i] for i in sorted(pole.keys())]
for i in range(1,n):
    for k in range(i):
        if lines[i] > lines[k]:
            length[i] = max(length[i], length[k] + 1)
print(n - max(length))