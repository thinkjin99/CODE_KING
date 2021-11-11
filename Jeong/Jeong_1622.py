strings = input()
def unpack(start_,end,k):
    res,last = 0,0
    is_open,is_close = False,False
    open_cnt,close_cnt = 0,0
    for i,s in enumerate(strings[start_:end], start = start_):
        if s == '(':
            if not is_open:
                open_index = i
                is_open = True
            open_cnt += 1

        if s == ')':
            close_cnt += 1
            if close_cnt == open_cnt: #짝이 맞는 괄호를 찾으면 괄호를 닫아준다.
                close_index = i
                is_close = True
        
        else:
            if not is_open: #괄호 밖에 존재하는 요소들을 카운트 
                last += 1

        if is_close and is_open: #괄호가 열리고 닫혔으면, 재귀 호출한다.
            res += unpack(open_index + 1, close_index, int(strings[open_index - 1]))
            last -= 1 #k의 경우 카운트 해주면 안되므로 k의 경우를 빼준다.
            #괄호가 열리고 닫히는 경우가 다시 존재 할 수 있으므로 재 초기화 해준다.
            close_cnt = 0
            open_cnt = 0
            is_close = False
            is_open = False

    return (res + last) * k

res = unpack(0,len(strings),1)

print(res)