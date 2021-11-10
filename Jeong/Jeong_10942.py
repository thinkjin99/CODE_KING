import sys
input = sys.stdin.readline
n = int(input())
arr = input().split()
dp = [[-1 for _ in range(n)] for _ in range(n)]
def DFS(start,end):
    if dp[start][end] != -1: #회문이거나 회문이 아니라는 것이 저장돼 있으면 저장된 값을 반환한다.
        return dp[start][end]
    
    if end - start <= 1:
        return 1 if arr[start] == arr[end] else 0
    
    if arr[start] == arr[end] and DFS(start + 1, end - 1): #내부에 존재하는 구문도 회문이면 회문으로 판단한다.
        dp[start][end] = 1
        return 1
    else:
        dp[start][end] = 0 #회문이 아니라는 것을 저장해준다.
        return 0

for _ in range(int(input())):
    s,e = map(int,input().split())
    print(DFS(s-1,e-1))