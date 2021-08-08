import sys
def find_set(v,set_list):
    for index,v_set in enumerate(set_list):
        if v in v_set:
            v_index = index
            break
    return v_index #u와 v가 각각 몇번 째 집합에 위치해 있는지 반환

n = int(input())

edges = []
for i in range(n):
    for j,w in enumerate(map(int,sys.stdin.readline().split())):
        if w > 0:
            edges.append((i,j,w))

set_list = [set([i]) for i in range(n)]
edges.sort(key = lambda weight: weight[2])
res = 0

for u,v,w in edges:
    u_index = find_set(u,set_list); v_index = find_set(v,set_list)
    if u_index != v_index:
        set_list[u_index] = set_list[u_index].union(set_list[v_index]) #합집합으로 값을 덮어 씌움
        set_list = set_list[:v_index] + set_list[v_index + 1:]
        res += w
        
print(res)

    



