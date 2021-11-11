import sys
input = sys.stdin.readline
n,k = map(int,input().split())
stats = []

for _ in range(n):
    stats.append([int(i) for i in input().split()])

res = float('inf')
for s in range(n):
    str_ = stats[s][0]
    for d in range(n):
        dex_ = stats[d][1]
        int_ = []
        for s,d,i in stats:
            if str_ >= s and dex_ >= d: #현재 선택한 str과 dex의 크기가 크다면
                int_.append(i) #조건에 만족하는 int값을 추가해준다.
        
        if len(int_) >= k:
            int_.sort()
            sum_of_stat = str_ + dex_ + int_[k-1]
            res = min(res,sum_of_stat)

print(res)