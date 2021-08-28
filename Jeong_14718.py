import sys
input = sys.stdin.readline
n,k = map(int,input().split())
stats = [[] for _ in range(3)]

for _ in range(n):
   for i,s in enumerate([int(i) for i in input().split()]):
       stats[i].append(s)

def check_count():
    x,y,z = [sorted(s) for s in stats] #3개의 스텟을 오름차순으로 정렬
    stat_data = []
    for i in range(n):
        temp = []
        for s in stats:
            temp.append(s[i])
        stat_data.append(temp)

    res = float('inf')
    for x_ in x:
        for y_ in y:
            for z_ in z:
                count = 0
                for s in stat_data:
                    str_,int_,dex_ = s
                    if str_ <= x_ and int_ <= y_ and dex_ <= z_:
                        count += 1
                    if count >= k: res = min(res,(x_ + y_ + z_))
    return res

res = check_count()
print(res)