import sys
sys.setrecursionlimit(10**8)
N = int(input())
visited = [False for _ in range(N+1)]
node_list = [[] for _ in range(N+1)]
node_adopter_count = [[0,0] for _ in range(N+1)] #각 노드별 얼리어답터 수를 저장한다.

for _ in range(N-1):
    u,v = map(int,sys.stdin.readline().split())
    node_list[u].append(v)
    node_list[v].append(u)

def check_adopter(current):
    visited[current] = True
    node_adopter_count[current][0] = 1 #현재 노드가 얼리어답터이다.
    node_adopter_count[current][1] = 0 #현재 노드가 얼리어답터가 아니다.
    for i in node_list[current]:
        if visited[i] == False: #방문하지 않은 정점일 경우
            #방문하지 않은 자식이 존재할 경우 아래로 내려간다.
            check_adopter(i)
            #얼리어답터인 경우 서브트리에 존재하는 최소 얼리어답터 수를 더해준다,
            node_adopter_count[current][0] += min(node_adopter_count[i][0],node_adopter_count[i][1])
            #얼리어답터가 아닌 경우 자식이 무조건 얼리어답터여야 하기에 서브트리가 얼리어 답터인 경우의 수를 더 해준다.
            node_adopter_count[current][1] += node_adopter_count[i][0]
    
check_adopter(1) #1을 루트로 가정 양방향 그래프이기에 무엇이 루트이든 관계 없다.
#1이 얼리어답터인 경우와 아닌 경우 중 최소 값을 출력한다.
print(min(node_adopter_count[1][0],node_adopter_count[1][1]))
