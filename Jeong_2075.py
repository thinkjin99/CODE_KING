import heapq
N = int(input())
columns = [[] for _ in range(N)]
for _ in range(N):
    for i,j in enumerate(list(map(int, input().split()))):
        columns[i].append(j) #colum으로 배열을 저장하고 싶어서.

h = [((col[-1] * -1 ,index)) for index,col in enumerate(columns)]

heapq.heapify(h)

for i in range(N):
    Nmax,index = heapq.heappop(h)
    columns[index].pop()
    if columns[index]:
        heapq.heappush(h,(columns[index][-1] * -1 ,index))

print(Nmax * -1)