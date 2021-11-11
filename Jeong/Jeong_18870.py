n = int(input())
nums = [int(i) for i in input().split()]
compress = dict()
for i,n in enumerate(sorted(set(nums))):
    compress[n] = i
res = [compress[n] for n in nums]
print(*res)