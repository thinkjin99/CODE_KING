import heapq
for _ in range(int(input())):
    n = int(input())
    files = [int(i) for i in input().split()]
    heapq.heapify(files)
    res = 0
    while len(files) > 1:
        cost = heapq.heappop(files) + heapq.heappop(files) # 합칠 파일 추출
        res += cost #결과 값에 비용 갱신
        heapq.heappush(files,cost) #합친 파일 큐에 다시 투입
    print(res)