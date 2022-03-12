import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    nums = [int(i) for i in input().split()]
    even = len(list(filter(lambda x: x % 2 == 0, nums)))
    if even >= 2:
        print('R')
    else:
        print('B')