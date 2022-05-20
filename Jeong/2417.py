n = int(input())
left = 0
right = n // 2
while left <= right:
    mid = (left + right) // 2
    power = mid * mid
    if power < n:
        left = mid + 1
    elif power > n:
        right = mid - 1
    else:
        print(mid)
        break
else:
    print(left)
