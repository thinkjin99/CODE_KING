import sys
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int,input().split())
user_sequence = [int(i) for i in input().split()]
multy_tap = []
product_index = defaultdict(list) #제품의 사용 시간을 저장한 딕셔너리
res = 0
for i,u in enumerate(user_sequence): 
    product_index[u].append(i)

for u in user_sequence:
    if u in multy_tap: #동일한 원소가 들어오면 인덱스를 갱신해준다.
        product_index[u].pop(0)
        continue

    if len(multy_tap) == n:
        mul_u = multy_tap[0]
        for m in multy_tap:
            if not product_index[m]: #만약 전부 사용했을 경우 최우선적으로 제거한다.
                mul_u = m
                break
            #더 이상 사용하는 제품이 없을 경우 가장 늦게 재사용하는 제품을 제거한다.
            mul_u = mul_u if product_index[mul_u][0] > product_index[m][0] else m
        multy_tap.remove(mul_u)
        res += 1
        
    multy_tap.append(u)
    product_index[u].pop(0)
print(res)