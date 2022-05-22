k, n = [int(i) for i in input().split()]
lines = [int(input()) for i in range(k)]
left = 1
right = max(lines)
while left <= right:
    mid = (left + right) // 2
    count = sum([l // mid for l in lines if l >= mid])
    if count < n:
        right = mid - 1
    elif count >= n:
        left = mid + 1
else:
    print(right)