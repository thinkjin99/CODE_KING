import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = n
cnt = 0
while True:
    m = (m % 10) * 10 + (m % 10 + m // 10) % 10
    cnt += 1
    if m == n:
        print(cnt)
        break

