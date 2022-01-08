import sys
input = sys.stdin.readline
def dfs(n,first,second):
    #alomst same as fibo prob 
    #main idea is using // operator in recursion to avoid calculate every single step
    #p and q always bigger than 2 so max recusrion is log 2 (10^12) = 12 * log2(10)
    if n in dp_dict.keys():
        return dp_dict[n]
    dp_dict[n] = dfs(n // first, first, second) + dfs(n // second, second, first)
    return dp_dict[n]

n,p,q = map(int, input().split())
dp_dict = {0:1}
dfs(n,p,q)
print(dp_dict[n])
