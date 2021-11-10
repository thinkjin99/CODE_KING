import sys
from operator import itemgetter
loc = [tuple(map(int,sys.stdin.readline().split())) for i in range(int(input()))]
res = ''
for i,j in sorted(loc,key = itemgetter(1,0)): #itemgetter로 sorted key설정 가능
    res += f"{i} {j}\n"
print(res)
# https://docs.python.org/3/howto/sorting.html