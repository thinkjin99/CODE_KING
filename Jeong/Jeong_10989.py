import sys
arr = [0 for _ in range(int(10001))]
for i in range(int(input())):
    arr[int(sys.stdin.readline())] += 1
for i,j in enumerate(arr):
    print(f"{i}\n" * j,end = '')