import sys
input = sys.stdin.readline
n = int(input())
num_dict = {}
for i in input().split():
    if i not in num_dict:
        num_dict[int(i)] = 1
print(*sorted(list(num_dict.keys())))
