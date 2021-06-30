import sys
from operator import itemgetter
loc = {(lambda x: (x,len(x)))(sys.stdin.readline()) for _ in range(int(input()))}
#중복처리를 위해 set을 사용한다.
res = ''
for i,j in sorted(loc,key = itemgetter(1,0)): #itemgetter로 sorted key설정 가능
    res += f"{i}"
print(res)
# https://docs.python.org/3/howto/sorting.html