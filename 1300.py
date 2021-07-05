import heapq
def findK(h,k):
    numCount = 0
    for i in range(1,N+1):
        heapq.heapreplace(h,(i*i))
        numCount += 1
        for j in range(i+1,N+1):
            if h[0] < i*j:
                heapq.heapreplace(h,(i*j))
            numCount += 2
            if numCount >= k:
                return h[0]
    return h[0]

if __name__ =='__main__':
    N = int(input())
    h = [0 for _ in range(N)]
    k = 7
print(findK(h,k))