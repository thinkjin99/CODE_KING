def getHead(node, cnt): # 헤드 구해주는 함수
    global head_list
    if head_list[node] != node:
        return getHead(head_list[node], cnt+1)
    else:
        # 여기에서의 cnt는 깊이를 말하는 거랄까,,,
        return (node, cnt)

while True:
    M, N = map(int, input().split())

    # ㅋㅋ 이 종료조건 이상해~
    if M==0 and N==0:
        break

    roads = []  # 아낀 돈 구해주기 위한,,,
    total_arr = []
    for i in range(N):
        a, b, c = map(int, input().split())
        roads.append(c)
        total_arr.append((a, b, c))

    # 거리 기준으로 정렬
    total_arr = sorted(total_arr, key = lambda dist:dist[2])
    # 각 node에 대한 head node 본인으로 초기화
    head_list = [i for i in range(M)]

    res = 0
    for elec in total_arr:
        verA, verB, dist = elec
        aHead, aCnt = getHead(verA, 0)
        bHead, bCnt = getHead(verB, 0)

        if aHead != bHead:
            res += dist
            # 깊이가 더 깊은 거에 짧은 거 넣어줄거야!
            if aCnt >= bCnt:
                head_list[bHead] = aHead
            else:
                head_list[aHead] = bHead

    print(sum(roads) - res)
