import sys
k = int(input())
nums_index_dict = {} #각 숫자별 인덱스를 저장하는 사전
nums = list(map(int,sys.stdin.readline().split()))
good_number = {}
for i,n in enumerate(nums):
    if n not in nums_index_dict:
        nums_index_dict[n] = []
    nums_index_dict[n].append(i) #딕셔너리에 해당 수를 갖는 인덱스를 저장
    good_number[n] = False

for i in range(k):
    for j in range(i+1,k):
        sum_of_num = nums[i] + nums[j]
        if sum_of_num in nums_index_dict:
            not_zero = None
            if 0 == nums[i] or 0 == nums[j]: #둘중에 하나는 0이여야 같은 수가 등장한다.
                if nums[i] == 0: not_zero = nums[j] #0이 아닌 수를 찾는다.
                else: not_zero = nums[i]
            else:
                good_number[sum_of_num] = True #둘다 0이 아니면 인덱스와 값이 동일한 수일 수 없으므로 종료한다.
                continue
            #이후에 취급하는 경우는 더하는 두 수중에 1개 이상의 0이 존재하는 경우이다.
            #같은 값이 등장하기에, 인덱스를 고려해줘야한다.
            if nums[i] == nums[j]: #0이 중복돼 들어올 떄
                if len(nums_index_dict[nums[i]]) - 2 > 0: #0이 여러 개일 경우 2개 보다 많은 0이 존재하면 좋은 수가 된다.
                    good_number[sum_of_num] = True
            elif len(nums_index_dict[not_zero]) > 1: #0과 N의 합의 형태로 표현 될 때
                good_number[sum_of_num] = True
res = 0
for i in nums:
    if good_number[i]:
        res += 1

print(res)
