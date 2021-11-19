import sys
input = sys.stdin.readline
n = int(input())
nums = [int(i) for i in input().split()]
operators = [int(i) for i in input().split()]
min_res, max_res = (123456789,-123456789)
def operating(accumulate,oper_index,new_num):
    res = 0
    if oper_index == 0: 
        res = accumulate + new_num
    elif oper_index == 1:
        res = accumulate - new_num
    elif oper_index == 2:
        res = accumulate * new_num
    elif oper_index == 3:
        if accumulate < 0:
            res = abs(accumulate) // new_num
            res *= - 1
        else:
            res = accumulate // new_num
    return res 

def backtracking(accumulate, operators, new_num_index):
    global min_res, max_res
    if new_num_index == len(nums) - 1:
        if accumulate < min_res: #하나의 숫자가 최대이자 최소일 수도 있다.
            min_res = accumulate
        if accumulate > max_res:
            max_res = accumulate
        return

    for i,o in enumerate(operators):
        if o: #연산자가 존재하면 깊이를 내려간다.
            operators[i] -= 1
            backtracking(operating(accumulate, i, nums[new_num_index + 1]), operators, new_num_index + 1)
            operators[i] += 1
    return
backtracking(nums[0],operators,0)
print(max_res)
print(min_res)


