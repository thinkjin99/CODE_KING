N = int(input())
arr = list(map(int, input().split()))

prevSize = 0
tempArr = []

for i in range(1, N):   # 초반의 type 확인 위함
    tempArr.append(arr[i-1])
    if arr[i] != arr[i-1]:
        if arr[i] > arr[i-1]:   # 커지면 0
            gotype = 0
        else:   # 작아지면 1
            gotype = 1
        break

for i in range(len(tempArr), N):    # 처음에 tempArr 어느정도 초기화해뒀으니,,,
    if arr[i] > arr[i-1] and gotype == 0:   # 증가하고 type도 증가
        tempArr.append(arr[i])

    elif arr[i] > arr[i-1] and gotype == 1: # 증가하는데 type은 감소일 때
        prevSize = max(prevSize, len(tempArr))  # 더 큰 값 저장
        tempArr = [arr[i-1]] * tempArr.count(arr[i-1])  # 겹치는 수 고려해서 새로운 tempArr 초기화
        tempArr.append(arr[i])  # 현재 값 더해줌
        gotype = 0  # 작아지는 거에서 커지는 걸로 변환

    elif arr[i] < arr[i-1] and gotype == 1: # 감소하고 type도 감소일 때
        tempArr.append(arr[i])

    elif arr[i] < arr[i-1] and gotype == 0: # 감소하는데 type은 증가일 때
        prevSize = max(prevSize, len(tempArr))
        tempArr = [arr[i-1]] * tempArr.count(arr[i-1])
        tempArr.append(arr[i])
        gotype = 1  # type 변환

    elif arr[i] == arr[i-1]:    # 이전 값과 같을 땐
        tempArr.append(arr[i])  # 아 묻지도 따지지도 말고~ tempArr에 더해주삼

# 이거때문에 막판에 여러 번 틀렸음ㅋ 맨 마지막에 tempArr의 길이랑 비교하는 부분 필요했음
print(max(prevSize, len(tempArr)))  
