import sys
from operator import itemgetter
if __name__ == '__main__':
    N = int(input())
    temp = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
    start = [(i[1],1) for i in temp]
    end = [(i[2],-1) for i in temp]
    schedules = start + end   
    schedules.sort()

    maxAc,accumulate = (1,0)
    before = schedules[0][0] #이전에 위치해 있던 값
    res = 0 # 같은 수 블럭의 합을 저장
    for i in range(len(schedules) + 1): #마지막 요소를 위해 한바퀴 더 돌아야함
        if i!= len(schedules) and schedules[i][0] == before: #이전에 위치해 있던 값과 동일하다면
            res += schedules[i][1] 
            continue
        else:
            accumulate += res
            if maxAc < accumulate:
                maxAc = accumulate
            if i!= len(schedules):
                res = schedules[i][1] #같은 수 블럭의 값 초기화
                before = schedules[i][0] #위치 수정

    # index = 0
    # while index < len(schedules):
    #     now = schedules[index][0]
    #     counts = 0
    #     for i in schedules[index:]:
    #         if now == i[0]:
    #             counts += 1
    #         break
                
    #     accumulate = 0
    #     for j in schedules[index: index + counts]:
    #         accumulate += j[1]
    #     accumulate += accumulate
    #     if accumulate > maxAc:
    #         maxAc = accumulate
    #     index += counts
    print(maxAc)

        