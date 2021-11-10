n = int(input())
p = 2
q = 1
res = 3
for i in range(1,n):
    res = 2 * p + 3 * q
    temp = p
    p = p + 2 * q
    q = temp + q
print(res % 9901)