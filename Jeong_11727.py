n = int(input())
front,back = 1,3
for i in range(1,n):
    front,back = back, front * 2 + back
else: print(front % 10007)