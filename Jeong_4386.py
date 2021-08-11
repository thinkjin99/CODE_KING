import sys
import math
from itertools import combinations

def find_compress(node):
    node_ = node
    while node != disjoint_tree[node]: # iterates until node reaches to root node 
        node = disjoint_tree[node]
    #After itertation node must be reached to root so node varaiable must be root
    
    while node_ != disjoint_tree[node_]: # during find compress path
        p_node = disjoint_tree[node_]
        disjoint_tree[node_] = node # make node_ and every parents of it as a child of root
        node_ = p_node
    
    return node

def weighted_union(u,v):
    u_root = find_compress(u) #find root 
    v_root = find_compress(v)
    if tree_size[u_root] > tree_size[v_root]: #compare the size of subset
        disjoint_tree[v_root] = u_root #make smaller subset as a child of big subset
        tree_size[u_root] += tree_size[v_root]
    else:
        disjoint_tree[u_root] = v_root
        tree_size[v_root] += tree_size[u_root]

    return

f = sys.stdin
n = int(input())
stars = [tuple(map(float,f.readline().split())) for _ in range(n)] #별들의 좌표를 저장해 놓는다
edges = []
disjoint_tree = [i for i in range(n)] #tree에는 부모요소가 한개 존재하므로 모든 트리를 하나의 배열에 표현할 수 있다.
tree_size = [1 for _ in range(n)]
for start,end in combinations(list(range(n)),2):
        s_x, s_y = stars[start] # 기준점의 좌표
        e_x, e_y = stars[end] # 비교점의 좌표
        distance = math.sqrt((s_x - e_x) ** 2 + (s_y - e_y) ** 2)
        edges.append((start,end,distance)) #도출한 별들 간의 거리를 edge에 넣어준다.
        #거리를 정렬기준으로 삼아야 하기에 가장 앞에 넣어준다.

res,edge_count = (0,0)
for u,v,w in sorted(edges,key=lambda x: x[2]):
    if edge_count >= n - 1:
        break
    u_root = find_compress(u); v_root = find_compress(v)
    if u_root == v_root: continue
    weighted_union(u,v)
    res += w; edge_count += 1

print(res)