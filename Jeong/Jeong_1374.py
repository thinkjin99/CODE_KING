import sys
from operator import itemgetter
def updateMax(ongoingMeetings,roomNums,sameTime):
    ongoingMeetings += sameTime #동일한 시간대에 존재하는 회의의 수를 진행 중인 회의 수에 더해준다.
    if roomNums < ongoingMeetings: #회의실이 진행 중인 회의 수보다 작으면
        roomNums = ongoingMeetings #회의실의 수 갱신
    return ongoingMeetings,roomNums

if __name__ == '__main__':
    N = int(input())
    temp = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
    schedules = [(time[0],1) for time in temp] + [(time[1],-1) for time in temp]
    schedules.sort() #시간을 기준으로 정렬한다.
    roomNums,ongoingMeetings = (1,0) #회의실 수, 시간 별로 진행중인 회의의 수
    before = schedules[0][0]
    sameTime = 0
    for time,meetingCount in schedules: #마지막 요소를 위해 한바퀴 더 돌아야함
        if time == before: #동일 시간에 존재하는 회의라면
            sameTime += meetingCount #같은 시간에 존재하는 회의의 합
            continue
        else:
            ongoingMeetings,roomNums = updateMax(ongoingMeetings,roomNums,sameTime)
            #같은 시간에 존재하는 회의가 아니라면 회의실 수 업데이트
            before = time
            sameTime = meetingCount
    print(updateMax(ongoingMeetings,roomNums,sameTime)[1])

        