from itertools import permutations

N, M = map(int, input().split())

arr = list(range(1,N+1))

# 내장함수 사용
# c = list(permutations(range(1,N+1), M))
# for i in range(len(c)):
#     c[i] = list(c[i])
#     for j in range(M):
#         print(c[i][j], end=" ")
#     print()

# 재귀함수 사용
def recur(nums, cnt):
    global M, arr   # 이전에 정의해둔 값 사용 위해 전역변수로 선언
    if(cnt==M): # 종료 조건
        for i in range(len(nums)):
            print(nums[i], end=" ")  # 원소 출력
        print()
        return
    

    for i in arr:   # 배열 돌면서
        if(str(i) not in nums): # 만약 i값이 이전에 저장해둔 순열에 없을 경우
            nums+=str(i)    # 값 추가
            recur(nums, cnt+1)  # 재귀함수 호출
            
            # 이전 단계로 돌아가서 값 있는지 확인하고 추가하고,,, 하기 위해서 제일 마지막에 추가된 값 삭제해줌
            length = len(nums)
            nums = nums[:length-1]


temp = ""
recur(temp, 0)
