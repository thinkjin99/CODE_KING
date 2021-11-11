import sys
if __name__ =='__main__':
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    left,right = (1,k)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(1,n + 1):
            cnt += min(mid // i,n)
        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    print(ans)
