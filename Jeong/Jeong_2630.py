def slicePaper(field,s_row,e_row,s_col,e_col): # start,end
    if s_row >= e_row or s_col >= e_col: #잘린 종이의 크기가 1이면
        if field[s_row][s_col] > 0: 
            return (1,0) #값이 1이면 블루를 리턴
        else: return (0,1)
    mid_row = (s_row + e_row) // 2
    mid_col = (s_col + e_col) // 2 
    #4등분을 계속해서 진행한다.
    r1 = slicePaper(field,s_row, mid_row, s_col, mid_col) #1사분면 
    r2 = slicePaper(field,s_row , mid_row, mid_col + 1, e_col) #2사분면
    r3 = slicePaper(field, mid_row + 1, e_row, s_col, mid_col) #3사분면
    r4 = slicePaper(field, mid_row + 1, e_row, mid_col + 1, e_col) #4사분면
    blue,white = (0,0)
    for r in [r1,r2,r3,r4]: #사분면에 각각 존재하는 색 종이들의 수를 합해준다.
        blue += r[0]
        white += r[1]
    if blue == blue + white: blue = 1 #해당 사분면에 파란색만 존재한다면 큰 파란 색종이 1개
    elif white == blue + white: white = 1 #해당 사분면에 흰색만 존재한다면 큰 하얀 색종이 1개
    return (blue,white) #해당 구역을 4등분 하는 과정을 마무리 했으므로 해당구역의 색종이 수를 반환 해준다.
  

if __name__ == '__main__':
    n = int(input())
    field = []
    for i in range(n):
       data  = list(map(int,input().split()))
       field.append(data)
    blue,white = slicePaper(field,0,n-1,0,n-1)
    print(white)
    print(blue)
