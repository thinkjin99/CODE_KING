from collections import defaultdict
dic = defaultdict()
for _ in range(10):
    n = int(input())
    dic[n % 42] = 1
print(len(dic.keys()))