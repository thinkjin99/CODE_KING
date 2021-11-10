import sys
input = sys.stdin.readline
def tsp(D):
    N = len(D)
    INF = float('inf')
    dp = [[None] * (2 ** N) for _ in range(N)] #부분집합의 수만큼 존재해야한다.
    path = [[None] * (2 ** N) for _ in range(N)] #부분집합의 수만큼 존재해야한다.
    VISITED_ALL = (1 << N) - 1 #모든 비트가 1인 경우이다.
    
    def find_path(last, visited):
        if visited == VISITED_ALL:
            return D[last][0] or INF #다시 처음으로 돌아오는 경우를 계산해줘야 한다.
        
        if dp[last][visited]: #이미 갖고 있는 값이면 굳이 연산할 필요 없다.
            return dp[last][visited]
        
        tmp = INF
        city_num  = None
        for city in range(N):
            if visited & (1 << city) == 0 and D[last][city] != 0:
                mid_res = find_path(city, visited | (1 << city)) + D[last][city] #방문한 도시의 비트는 켜준다.
                if mid_res < tmp:
                    tmp = mid_res
                    city_num = city #다음 방문할 도시를 초기화 해준다.

        path[last][visited] = city_num #도시가 정해지면 다음 방문할 도시를 해당 도시로 초기화 한다.
        dp[last][visited] = tmp #visited의 노드들을 모두 포함하고 city까지 도달하는 최소 값
        return dp[last][visited] #저장한 최소 값을 반환한다.
    #처음 호출한 함수가 가장 늦게 종료되므로 최종 값도 첫 호출 위치에 저장된다.
    find_path(0,1) # 0번도시에서 시작하고 0번은 도시는 방문했으므로 visitied  = 1 << 0 , 1이 된다.
    return dp[0][1], path

def print_path(path):
    visited = 1 << 0
    next_city = path[0][visited] #path 가장 처음 시작점 이후로 방문하는 도시
    res = []
    while next_city:
        res.append(next_city + 1)
        visited = visited | 1 << next_city #해당 도시를 방문처리 해준다.
        next_city = path[next_city][visited]
    return res

if __name__ == '__main__':
    D = [[int(i) for i in input().split()] for _ in range(int(input()))]
    cost,path = tsp(D)
    p = print_path(path)
    print(cost)
    print(1,*p,1)