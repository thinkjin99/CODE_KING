cnt  = 0
res = []
def hanoi(n,start,end):
    if n < 1: return
    global cnt
    cnt += 1
    via = 6 - (start + end) #start와 end를 지나지 않는 점이 경로이다.
    hanoi(n - 1, start, via)
    res.append(f"{start} {end}")
    hanoi(n - 1, via, end)



if __name__ == '__main__':
    n = int(input())
    hanoi(n,1,3)
    print(cnt)
    for s in res:
        print(s)

    
