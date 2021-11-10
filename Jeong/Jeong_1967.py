import sys
class Node:
    def __init__(self) -> None:
        self.childs_and_weights = [] #자식과 자식까지의 가중치를 튜플 형태로 저장한다.
        self.radius = [] #해당 노드까지 이르기 위한 최대 경로를 저장해 둔다. 지름을 만들기 위해선 2개의 최대 경로만 필요하다.

    def push_data(self,child,weight):
        self.childs_and_weights.append((child,weight)) #노드에 필요한 데이터들을 추가한다.

def append_radius(radius,weight): #radius 배열에는 크기가 큰 2개의 원소만 존재하고 있으면 된다.
    if len(radius) < 2: #radius의 크기가 2이하이면 요소를 더 추가해야 하므로
        radius.append(weight)
    else:
        min_radius = min(radius)
        if min_radius < weight: #최소 값과 교환 해준다 radius의 크기는 2이하 이다.
            index = radius.index(min_radius)
            radius[index] = weight

def get_tree_radius(key, parent_node_dict):
    radius = parent_node_dict[key].radius #현재 입력된 key노드 까지의 최대 가중치
    for child,weight in parent_node_dict[key].childs_and_weights: #입력받은 데이터와 key 노드에 존재하는 데이터를 비교
        if child not in parent_node_dict: #자식이 존재하지 않는 노드이기에 가중치를 바로 추가해주면 된다.
           append_radius(radius,weight)
        else:
            max_child_radius = parent_node_dict[child].radius[0] + weight #자식이 존재할 경우 자식의 최대 가중치 + 현재 노드의 가중치로 초기화 한다.
            append_radius(radius,max_child_radius)

    radius.sort(reverse = True) #radius를 정렬해준다. 최대 값이 가장 앞에 존재해야 한다.

if __name__ == '__main__':
    parent_node_dict = {}
    for _ in range(int(input()) - 1):
        key,child,weight = map(int,sys.stdin.readline().split())
        if key not in parent_node_dict:
            parent_node_dict[key] = Node()
        parent_node_dict[key].push_data(child,weight)
    
    for k in reversed(parent_node_dict.keys()): #말단 노드부터 시작해 모든 노드의 지름을 구한다.
        get_tree_radius(k,parent_node_dict)
        
    ans = 0
    for r in parent_node_dict.values():
        if ans < sum(r.radius):
            ans = sum(r.radius)
    print(ans)

