import sys
input = sys.stdin.readline
n = int(input())
card_list = {i:1 for i in input().split()}
k = int(input())
query_list = [i for i in input().split()]
print(*map(lambda x: 1 if x in card_list else 0, query_list))