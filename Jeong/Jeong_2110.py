import sys
n,c = map(int,sys.stdin.readline().split())
homes = sorted([int(sys.stdin.readline()) for _ in range(n)])
minGap = 1 #인접한 집들 간의 거리 이중 최소가 최소 거리이다.
maxGap = homes[-1] - homes[0]
ans = 0
while minGap <= maxGap:
    nowGap = (minGap + maxGap) // 2 #간격의 최대 최소
    count = 1
    nowLoc = homes[0]
    for home in homes: #간격이 유요한지 검증
        if home >= nowLoc + nowGap:
            count += 1
            nowLoc = home
    if count < c: #간격을 줄여서 호출한다.
        maxGap = nowGap - 1
    else:
       minGap = nowGap + 1
       ans = nowGap
print(ans)
         #간격안에 원하는 만큼 공유기를 배치할 수 있으면 종료
       



