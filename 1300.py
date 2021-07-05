import heapq
import sys
def findK(h,k):
    numCount = 0
    for i in range(1,N+1):
        heapq.heapreplace(h,i*i)
        numCount += 1
        if numCount >= k: return
        for j in range(i+1,N+1):
            if h[0] < (i * j):
                heapq.heapreplace(h,i*j)
            numCount += 2
            if numCount >= k: return

if __name__ =='__main__':
    N = int(sys.stdin.readline())
    h = [0 for _ in range(N)]
    k = int(sys.stdin.readline())
    findK(h,k)
    print(max(h[N//2:]))
