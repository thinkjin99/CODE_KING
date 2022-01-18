n = int(input())
childs = [int(input()) for _ in range(n)]
length = [1] * n #length list
for k in range(1, n):
    for i in range(k):
        if childs[i] < childs[k]: #compare max length in smaller numbers
            length[k] = max(length[k], length[i] + 1) #update length
print(n - max(length))