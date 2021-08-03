import sys
sys.setrecursionlimit(10**7)
def DFS(row,col,count):
        global ans
        '''
        각 지점마다 분기가 갈라지므로 경로도 전부 개별로 저장해줘야 한다. 
        이후의 결과가 영향을 미쳐선 안되기 떄문이다.
        '''
        ans = max(ans,count)
        for (horizon, vertical) in zip((-1,1,0,0),(0,0,1,-1)):
            next_row = row + horizon
            next_col = col + vertical
            if (0 <= next_row < n) and (0 <= next_col < m):
                if visited_letter[board[next_row][next_col]] != True: 
                    visited_letter[board[next_row][next_col]] = True #해당 알파벳을 경로에 추가
                    DFS(next_row,next_col,count+1)
                    visited_letter[board[next_row][next_col]] = False
        
        # print(path.keys(),board[row][col])

if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split())
    board  = [[] for _ in range(n)]
    ans =  1
    visited_letter = [False for _ in range(ord('A'),ord('Z')+1)]
    for i in range(n):
        for w in sys.stdin.readline().rstrip():
            board[i].append(ord(w) - 65)

    visited_letter[board[0][0]] = True
    DFS(0,0,1)
    print(ans)
