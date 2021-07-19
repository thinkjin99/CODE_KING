import sys
class Node:
    def __init__(self) -> None:
        self.child_weights = []
        self.radius = []
    def push_data(self,child,weight):
        self.child_weights.append((child,weight))
        # self.radius.append(weight)

def append_radius(radius,weight):
    if len(radius) < 2:
        radius.append(weight)
    else:
        min_radius = min(radius) #가중치의 최대는 100
        if min_radius < weight: #최소 값과 교환 해준다 radius의 크기는 2이하 이다.
            index = radius.index(min_radius)
            radius[index] = weight

def get_tree_radius(key, parent_node_dict):
    radius = parent_node_dict[key].radius
    for child,weight in parent_node_dict[key].child_weights:
        if child not in parent_node_dict:
           append_radius(radius,weight)
        else:
            max_child_radius = parent_node_dict[child].radius[0] + weight
            append_radius(radius,max_child_radius)

    if len(radius) > 1 and radius[0] < radius[1]:
        radius[1],radius[0] = radius[0],radius[1]     

if __name__ == '__main__':
    parent_node_dict = {}
    for _ in range(int(input()) - 1):
        key,child,weight = map(int,sys.stdin.readline().split())
        if key not in parent_node_dict:
            parent_node_dict[key] = Node()
        parent_node_dict[key].push_data(child,weight)
    
    for k in reversed(parent_node_dict.keys()):
        get_tree_radius(k,parent_node_dict)
        
    max_r = 0
    for r in parent_node_dict.values():
        if max_r < sum(r.radius):
            max_r = sum(r.radius)
    print(max_r)

