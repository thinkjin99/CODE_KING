import sys
n = int(input())
k = int(input())
sensors = list(map(int,input().split()))
sensors.sort()
gaps = [(sensors[i] - sensors[i - 1]) for i in range(1,len(sensors))] #인접 센서 간의 간격
gaps.sort(reverse = True) #간격을 크기 순으로 정렬한다.
distance = sensors[-1] - sensors[0] #전체 거리
for gap in gaps[:k - 1]:
    distance -= gap #크기가 큰 순서대로 간격을 추출한 뒤 전체 거리에서 빼준다.
print(distance) #K개의 간격을 전체거리에서 빼주면 최소 범위가 도출된다.

