def create_permu(arr, permu):
    if len(arr) == 0:
        max_gap = 0
        for bf, af in zip(permu[:-1], permu[1:]):
            max_gap +=  abs(bf - af)
        res[0] = max(res[0], max_gap)
        return
    else:
        for i, n in enumerate(arr):
            create_permu(arr[:i] + arr[i + 1:], permu + [n])

res = [0]
n = int(input())
nums = [int(i) for i in input().split()]
create_permu(nums, [])
print(res[0])
