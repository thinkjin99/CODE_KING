n = int(input())
loaf = sorted([int(input()) for _ in range(n)])
loaf = [i*l for i,l in zip(range(n,0,-1),loaf)]
print(max(loaf))