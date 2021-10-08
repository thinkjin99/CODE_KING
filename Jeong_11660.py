import sys
input = sys.stdin.readline
n,m = 4,3
matrix = [[int(i) for i in input().split()] for _ in range(n)]
querys = [[int(i) for i in input().split()] for _ in range(m)]
columns = [[row[i] for row in matrix] for i in range(n)]
row_sum = [sum(r) for r in matrix]
col_sum = [sum(c) for c in columns]

for q in querys:
    a,b,c,d = q
    if a == c and b == d:
        print(matrix[a-1][b-1])
        continue
    elif a == c and b != d:
        print(sum(matrix[a][b:d]))
    elif a != c and b == d:
        

