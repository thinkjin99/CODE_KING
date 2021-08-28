import sys
input = sys.stdin.readline
n,k = map(int,input().split())
stats = [[] for _ in range(3)]

for _ in range(n):
   for i,s in enumerate([int(i) for i in input().split()]):
       stats[i].append(s)

sorted_stats = [sorted(s) for s in stats] #3개의 스텟을 오름차순으로 정렬
standard = [s[k -1] for s in sorted_stats] #각 스텟의 k번째 값을 추출 각 스텟들이 해당 위치의 값보단 커야한다.
filtered_index = range(n) #기준을 모두 통과한 인덱스들을 저장할 변수
for stat_,std in zip(stats,standard):
    filtered_index = filter(lambda x: stat_[x] >= std, filtered_index) #해당 스텟이 기준점을 통과하는지 검사

res = float('inf')
for f in filtered_index:
    res = min(res,sum([s[f] for s in stats]))
print(res)