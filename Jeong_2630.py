def slicePaper(field,s_row,e_row,s_col,e_col): # start,end
    if s_row >= e_row or s_col >= e_col:#잘린 배열의 크기가 1이면
        if field[s_row][s_col] > 0: 
            return (1,0)
        else: return (0,1)
    mid_row = (s_row + e_row) // 2
    mid_col = (s_col + e_col) // 2 
    r1 = slicePaper(field,s_row, mid_row, s_col, mid_col)
    r2 = slicePaper(field,s_row , mid_row, mid_col + 1, e_col)
    r3 = slicePaper(field, mid_row + 1, e_row, s_col, mid_col)
    r4 = slicePaper(field, mid_row + 1, e_row, mid_col + 1, e_col)
    res = [r1,r2,r3,r4]
    blue = 0
    white = 0
    for i in res:
        blue += i[0]
        white += i[1]
    if blue == blue + white: blue = 1
    elif white == blue + white: white = 1
    return (blue,white)
  

if __name__ == '__main__':
    n = int(input())
    field = []
    for i in range(n):
       data  = list(map(int,input().split()))
       field.append(data)
    blue,white = slicePaper(field,0,n-1,0,n-1)
    print(white)
    print(blue)
