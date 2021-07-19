res = {}
def level_order(nodes,height):
    if len(nodes) > 0:
        root = len(nodes) // 2
        if height in res:
            res[height].append(nodes[root])
        else: res[height] = [nodes[root]]
        level_order(nodes[:root],height + 1)
        level_order(nodes[root + 1:],height + 1)
nodes = [1,6,4,3,5,2,7]
level_order(nodes,0)
for k,v in res.items():
    print(k,v)