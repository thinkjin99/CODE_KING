import sys
class Node:
    def __init__(self) -> None:
        self.child_weights = []
        self.radius = []
    def push_data(self,child,weight):
        self.child_weights.append((child,weight))
        # self.radius.append(weight)

def get_tree_radius(key, parent_node_dict):
    radius = parent_node_dict[key].radius
    for child,weight in parent_node_dict[key].child_weights:
        if child not in parent_node_dict:
            radius.append(weight)
        else:
            child_max_radius = parent_node_dict[child].radius.pop(0)
            radius.append(child_max_radius + weight)

    # parent_node_dict[key].radius = sorted(radius,reverse = True)

if __name__ == '__main__':
    parent_node_dict = {}
    for _ in range(int(input())):
        key,child,weight = map(int,sys.stdin.readline().split())
        if key not in parent_node_dict:
            parent_node_dict[key] = Node()
        parent_node_dict[key].push_data(child,weight)
    
    for k in reversed(parent_node_dict.keys()):
        get_tree_radius(k,parent_node_dict)
        print(parent_node_dict[k].radius)

    # for i,v in parent_node_dict.items():
    #     print(i, v.child_weights)
