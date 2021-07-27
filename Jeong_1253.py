import sys
def binary_search(num,point_standard,num_index,good_count):
    start = num_index 
    end = len(nums) - 1
    mid_point = 0
    while start <= end:
        mid = (start+end) // 2
        mid_point = mid
        if nums[mid] == num + point_standard:
            good_count.append(num_dict[nums[mid]])
            return True
        elif num + point_standard < nums[mid]:
             end = mid - 1
        else:
            start = mid + 1
    return mid_point

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    num_dict = {}
    for i in nums:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    good_count = []
    for i,n in enumerate(sorted(nums)): #맨 앞의 요소는 실행하지 않는다.
        start =  binary_search(n,nums[0],i,good_count) #최소 값을 통한 큰 수의 시작 범위 설정
        if i == 0 or start: continue
        end = binary_search(n,nums[i-1],i,good_count) #최대 값을 통한 큰 수의 끝 범위 설정
        if start and end:
            for j in range(start,end+1):
                if nums[j] - n in num_dict:
                    good_count.append(num_dict[nums[j]])

    print(sum(good_count)) 



        



