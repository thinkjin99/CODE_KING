n,m = map(int, input().split())
array = [[i for i in ''.join(input())] for _ in range(n)]
ans = -1
#공차를 기준으로 생각하면 쉽다.
def check_square(num):
    i_num = int(num)
    if (i_num ** 0.5).is_integer():
        return int(i_num)
    return -1
if n * m == 1:
    ans = max(check_square(*array[0]),ans)
else:
    for i in range(n):
        for j in range(m):
            for r_d in range(-n+1,n): #음수 공차도 고려해야한다.
                for c_d in range(-m+1,m):
                    if r_d == 0 and c_d == 0: continue
                    r_cur, c_cur = i,j
                    res = ''
                    while (0 <= r_cur < n) and (0 <= c_cur < m):
                        res += array[r_cur][c_cur]
                        ans = max(check_square(res),ans) #한칸 이동할 때 마다 제곱수 여부 확인
                        r_cur += r_d
                        c_cur += c_d
print(ans)