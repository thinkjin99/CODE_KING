strings = input()
def unpack(start,end,k):
    res,last = 0,0
    is_open,is_close = False,False
    open_cnt,close_cnt = 0,0
    for i,s in enumerate(strings[start:end],start = start):
        if s == '(':
            if not is_open:
                open_index = i
                is_open = True
            open_cnt += 1

        if s == ')':
            close_cnt += 1
            if close_cnt == open_cnt:
                close_index = i
                is_close = True
        
        else:
            if not is_open:
                last += 1

        if is_close and is_open:
            res += unpack(open_index + 1, close_index, int(strings[open_index - 1]))
            last -= 1
            close_cnt = 0
            open_cnt = 0
            is_close = False
            is_open = False

    return (res + last) * k

brackets_count = 0
res = unpack(0,len(strings),1)

print(res)