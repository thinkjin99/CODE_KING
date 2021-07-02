import sys
from operator import itemgetter

def binarySearch(schedules,start,end,n):
    mid = (end+start) // 2
    if n == schedules[mid][1]: return mid
    if schedules[mid][1] > n:
        return binarySearch(schedules,start,mid - 1,n)
    elif schedules[mid][1] < n:
        binarySearch(schedules,mid + 1,end,n)
    return mid

if __name__ == '__main__':
    N = int(input())
    schedules = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
    schedules = sorted(schedules,key = itemgetter(2,1))
    cnt = 0 #회의실 수

    while schedules:
        fast = schedules.pop(0) #가장 빨리 끝나는 회의
        #for 에서 remove호출 시 오류가 발생하기 떄문에
      
    print(schedules)

      # for i in schedules:
        #     if i[1] >= fast[2]: #이후 시작하는 회의 중 가장 일찍 끝나는 회의
        #         removed.append(i)
            
        #         fast = i
        # for r in removed:
        #     schedules.remove(r)