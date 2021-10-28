import sys
input = sys.stdin.readline
N = int(input())
MAX = 123456789
d = [tuple(map(int,input().split())) for _ in range(N)]
m = [[MAX for _ in range(N)] for _ in range(N)]
for i in range(N): m[i][i] = 0
for l in range(1,N): #부분 수열의 길이, 결합된 행렬의 수
    for i in range(N - l): 
        #i는 결합의 시작점을 의미한다. 끝 - 길이보단 적은 위치에서만 시작이 가능하다.
        j = i + l #j는 결합의 끝점을 의미한다.
        for k in range(i, j):#k는 i와 j의 중간에 놓인 점으로 행렬 결합을 분할하는 점을 의미한다.
            current = d[i][0] * d[k+1][0] * d[j][1]
            #(i,k) * (k, j) -> i * (k * j)
            m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + current)
            #시작점을 옮기고 길이를 늘려보며 모든 경우를 비교한다.
print(m[0][N-1])