
_blue = 0
_white = 0
def slicePaper(field,s_row,e_row,s_col,e_col): # start,end
    if s_row == e_row or s_col == e_col:#잘린 배열의 크기가 1이면
        if field[s_row][s_col] > 0: 
           return 1
        else: return 0
    r1 = slicePaper(field,s_row, e_row // 2, s_col, e_col )
    r2 = slicePaper(field,e_row // 2 ,e_row , s_col, e_col)
    # r3 = slicePaper(field,e_row // 2, e_row, s_col, e_col // 2)
    # r4 = slicePaper(field,e_row // 2, e_row, e_col // 2, e_col)
    white = 4 - r1 + r2 + r3 + r4
    blue = 4 - white
    if blue == 4: blue = 1
    elif white == 4: white = 1
    global _blue
    _blue += blue
    global _white
    _white += white
    return

if __name__ == '__main__':
    n = int(input())
    field = []
    for i in range(n):
       data  = list(map(int,input().split()))
       field.append(data)
    slicePaper(field,0,n-1,0,n-1)

