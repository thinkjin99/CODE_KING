import sys
input = sys.stdin.readline
n = int(input())
arrs = [int(i) for i in input().split()]
arrs.sort()
left = 0; right = n - 1
sum_tup = tuple()
ans = float('inf')
while left < right:   
    sum_ = arrs[left] + arrs[right]
    if abs(sum_) < ans:
        ans = abs(sum_)
        sum_tup = (arrs[left],arrs[right])
    if sum_ < 0:
        left += 1
    else:
        right -= 1
print(*sum_tup)