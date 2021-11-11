import sys
sys.setrecursionlimit(10**7)
def DFS(y_loc,x_loc,height):
    if (0 <= x_loc < n) and (0 <= y_loc < n):
        if visited[y_loc][x_loc] or height_arr[y_loc][x_loc] <= height:
            return
        visited[y_loc][x_loc] = True
        DFS(y_loc + 1,x_loc,height) #up
        DFS(y_loc - 1,x_loc,height) #down
        DFS(y_loc,x_loc + 1,height) #right
        DFS(y_loc,x_loc - 1,height) #left

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    height_arr = [[1 for _ in range(n)] for _ in range(n)]
    heights_dict = dict()
    for row in range(n):
        for col,h in enumerate(map(int,sys.stdin.readline().split())):
            height_arr[row][col] = h
            if h not in heights_dict:
                heights_dict[h] = [(row,col)]
            else: heights_dict[h].append((row,col)) #높이 별로 좌표를 저장

    heights = sorted(heights_dict.keys()) # 각 높이를 정렬
    safe_area_counts = [] # 안전 구역의 수

    for index,h in enumerate(heights): #h는 지금 검사하고자 하는 높이
        safe_hegihts = heights[index+1:] #안전구역이 될 수 있는 높이들
        count = 0

        if safe_hegihts: #안전구역이 될 수 있는 높이가 없다면 종료
            visited = [[False for _ in range(n)] for _ in range(n)]
            for k in safe_hegihts:
                for y_loc,x_loc in heights_dict[k]: #안전구역이 될 수 있는 높이를 갖는 좌표 추출
                    if visited[y_loc][x_loc]: continue
                    else:
                        DFS(y_loc,x_loc,h)
                        count += 1
        safe_area_counts.append(count)

    ans = max(safe_area_counts)
    
    if ans == 0: #모든 영역의 높이가 같은 경우
        print(1)
    else:
        print(ans)





    



