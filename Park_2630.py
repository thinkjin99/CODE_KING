N = int(input())

totalArray = []

for i in range(N):
    temp = input()
    # 얘가 입력받을 때 하나씩 빈칸 가지고 입력을 받더라고
    # 빈칸 제거 위한 코드
    tempList = []
    for i in range(len(temp)):
        if temp[i] != ' ':
            tempList.append(temp[i])
    totalArray.append(tempList)

index = 0
blue = 0
white = 0

def divide(size, row, col):
    global blue, white, totalArray  # 전역변수 선언
    newArray = []

    for i in range(size):   # 인자로 받은 값들 이용하여 배열 추출
        newArray.append(totalArray[row+i][col:(col+size)])

    # 새로 추출한 배열에 있는 원소값들의 개수 구하기 위함
    cntBlue = 0
    cntWhite = 0
    for i in range(size):
        cntBlue += newArray[i].count('1')
        cntWhite += newArray[i].count('0')

    if cntBlue == size*size:    # 전체가 다 1로 차있다면
        blue+=1
        return

    if cntWhite == size*size:   # 전체가 다 0으로 차있다면
        white+=1
        return

    size = size//2  # 배열의 크기를 이전/2로 점점 줄여나감.

    divide(size, row, col)  # 그 자리에서 사이즈만 작게 한 그 다음 배열 탐색 위함
    divide(size, row+size, col) # 이전 자리 기준 아래 위치의 배열 탐색 위함
    divide(size, row, col+size) # 이전 자리 기준 오른쪽 위치의 배열 탐색 위함
    divide(size, row+size, col+size)    # 이전 자리 기준 오른쪽 아래 배열 탐색 위함

divide(N, 0, 0)
print(white)
print(blue)
