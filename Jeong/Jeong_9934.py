import sys
def level_order(left,right,height):
    if left <= right:
        root = (left + right) // 2
        if height in level_dict:
            level_dict[height].append(nodes[root])
        else: level_dict[height] = [nodes[root]]
        level_order(left,root - 1,height + 1)
        level_order(root + 1,right,height + 1)

level_dict = {}
n = int(input())
nodes = sys.stdin.readline().split()
level_order(0,len(nodes) - 1,0)
for v in level_dict.values():
    print(" ".join(v))