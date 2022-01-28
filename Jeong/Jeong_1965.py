n = int(input())
boxes = [int(i) for i in input().split()]
length = [1] * n
for i in range(1,n):
	for j in range(i):
		if boxes[i] > boxes[j]:
			length[i] = max(length[i], length[j] + 1)
print(max(length))
