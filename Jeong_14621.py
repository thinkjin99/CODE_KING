import sys
f = sys.stdin
def find(u):
    u_ = u
    while u != disjoint_tree[u]: # iterates until u reaches to root u 
        u = disjoint_tree[u]
    
    while u_ != u: # during find compress path
        parent_u = disjoint_tree[u_]
        disjoint_tree[u_] = u # make u_ and every parents of it as a child of root
        u_ = parent_u

    return u

def union(u,v):
    u_root = find(u); v_root = find(v)
    if tree_size[u_root] > tree_size[v_root]:
        disjoint_tree[v_root] = u_root
        tree_size[u_root] += tree_size[v_root]
    else:
        disjoint_tree[u_root] = v_root
        tree_size[v_root] += tree_size[u_root]
    return

n,m = map(int,input().split())
univ_sex = f.readline().split()
edges = []
disjoint_tree = [i for i in range(n)]
tree_size = [1 for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,f.readline().split())
    u,v = u-1,v-1
    if univ_sex[u] == univ_sex[v]: continue #같은 성별의 대학교이면 continue 해야 한다.
    edges.append((u,v,w))

res,edge_cnt = (0,0)
for u,v,w in sorted(edges,key=lambda x: x[2]):
    if edge_cnt >= n - 1:
        break
    if find(u) != find(v):
        union(u,v)
        res += w; edge_cnt += 1

if edge_cnt < n-1:
    print(-1)

else: print(res)


