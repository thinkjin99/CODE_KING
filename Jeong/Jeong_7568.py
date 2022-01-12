n = int(input())
body = [tuple(map(int,input().split())) for _ in range(n)]
ranks = [0] * n
for i,(w,h) in enumerate(body):
    ranks[i] = len(list(filter(lambda wh: wh[0] > w and wh[1] > h, body))) + 1
print(*ranks)