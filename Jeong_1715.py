N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
before = nums.pop(0)
res = before if N == 1 else 0
for i in nums:
    before += i
    res += before
print(res)
