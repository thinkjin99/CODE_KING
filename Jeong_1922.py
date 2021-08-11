import sys
def find_compress(node):
    node_ = node
    while node != p_set[node]: # iterates until node reaches to root node 
        node = p_set[node]
    #After itertation node must be reached to root so node varaiable must be root
    
    while node_ != p_set[node_]: # during find compress path
        p_node = p_set[node_]
        p_set[node_] = node # make node_ and every parents of it as a child of root
        node_ = p_node
    
    return node

def weighted_union(u,v):
    u_root = find_compress(u) #find root 
    v_root = find_compress(v)
    if p_size[u_root] > p_size[v_root]: #compare the size of subset
        p_set[v_root] = u_root #make smaller subset as a child of big subset
        p_size[u_root] += p_size[v_root]
    else:
        p_set[u_root] = v_root
        p_size[v_root] += p_size[u_root]

    return

f = sys.stdin
n = int(input()); m = int(input())
edges = [tuple(map(int,f.readline().split())) for _ in range(m)]
p_set = [i for i in range(n + 1)] #set for union-find
p_size = [1 for _ in range(n + 1)]#size of each subset
res,edge_count = 0,0
for u,v,w in sorted(edges, key = lambda k: k[2]):
    if edge_count >= n - 1: #if count of edges in tree exceed n-1 break iteration
        break
    u_root = find_compress(u); v_root = find_compress(v)
    if u_root == v_root: continue
    weighted_union(u,v)
    res += w; edge_count += 1
print(res)