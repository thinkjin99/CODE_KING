import sys
import itertools
input = sys.stdin.readline
n,m = map(int,input().split())
MAX = 123456789
def get_distance(subset):
    all_chicken_distance = MAX #전체 치킨 거리
    for chicken in subset:
        subset_distance = 0 #해당 부분집합의 치킨 집들을 방문 했을 때의 치킨거리
        for h in houses: #각각의 집에서 치킨 집까지의 최단 거리를 구한다.
            h_x, h_y = h
            distance = MAX #각 집에서 치킨 집까지의 거리
            for c in chicken:
                c_x, c_y = chickens[c]
                distance = min(distance, abs(h_x - c_x) + abs(h_y - c_y))
            subset_distance += distance
        all_chicken_distance = min(all_chicken_distance, subset_distance)
    return all_chicken_distance
    
if __name__ == '__main__':
    city = [[0 for _ in range(n)] for _ in range(n)]
    chickens = []
    houses = []
    for i in range(n):
        for j,v in enumerate([int(i) for i in input().split()]):
            city[i][j] = v
            if v == 1:
                houses.append((i + 1, j + 1))
            elif v == 2:
                chickens.append((i + 1,j + 1))
    subsets = list(itertools.combinations(range(len(chickens)),m)) #치킨집의 경우의 수를 모두 구해준다.
    print(get_distance(subsets))
