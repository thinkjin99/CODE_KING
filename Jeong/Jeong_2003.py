import sys
n,m = map(int, sys.stdin.readline().split())
sequences = list(map(int,sys.stdin.readline().split()))
start,end = (0,0)
cnt = 0
part_sum = 0
while end <= n: #마지막 까지 더했을 때 확인하기 위해서
    if part_sum < m:
        if end == n : break
        part_sum += sequences[end]
        end += 1 #작을 경우 값의 크기를 늘려준다
    elif part_sum >= m:
        part_sum -= sequences[start]
        start += 1 #클 경우 값의 크기를 줄여준다.
    if m == part_sum: cnt += 1
print(cnt)
