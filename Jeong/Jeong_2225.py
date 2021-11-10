import sys
input = sys.stdin.readline
num,count = map(int,input().split())
dp = [[-1 for _ in range(count + 1)] for _ in range(num + count)]
def combination(n,k):
    if n == k or k == 0:
        return 1
    elif dp[n][k] != -1:
        return dp[n][k]
    dp[n][k] = combination(n-1,k) + combination(n-1,k-1)
    return dp[n][k]
#중복조합의 아이디어를 활용한다.
print(combination(num+count-1,count-1) % 1000000000)