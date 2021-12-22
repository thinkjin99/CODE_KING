N = int(input())

def hanoi(n, start, tmp, end):
    if(n==1):
        print(start, end)
        return
    else:
        hanoi(n-1, start, end, tmp)    # start에 있는 n-1번째까지의 원판을 tmp로 옮김
        print(start,end)   # 제일 큰 원판을 end로 옮김
        hanoi(n-1, tmp, start, end)    # 나머지 tmp에 있던 원판들 다 end로 옮기기

print(2**N-1)
hanoi(N, 1, 2, 3)