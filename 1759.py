n,m = input().split()
def Permutation(arr,path,moum,jaum,pathData):
    if(len(path) == int(n)): 
        for i in path:
            print(str(i) + " ",end = '')
        print()
        return
    for i in arr:
         #현재의 요소가 모음인지 확인
        index = arr.index(i)
        moum = [m for m in moum if m >= i] # 현재의 요소보다 큰 모음
        jaum = [j for j in jaum if j >= i]# 현재의 요소보다 큰 자음
        
        # print(i,moum)
        # print(i,jaum)
        nextM,nextJ = pathData
        # if i in 'aeiou': nextM += 1
        # else: nextJ += 1
        if len(moum) >= 1 - nextM and len(jaum) >= 2 - nextJ: #앞으로 가능한 모음 - 지금까지 지나온 모음 
            if i in 'aeiou': 
                nextM += 1
                moum = moum[1:]
            else: 
                nextJ += 1
                jaum = jaum[1:]
            # if int(n) - (nextM+nextJ) < len(moum) + len(jaum):
            Permutation(arr[:index] + arr[index + 1:],path + [i],moum,jaum,(nextM,nextJ))


if __name__ =='__main__':
    moum = []
    jaum = []
    arr = sorted([i for i in input().split()])
    for i in arr:
        if i in 'aeiou':
            moum.append(i)
        else: jaum.append(i)

    Permutation(arr,[],moum,jaum,(0,0))
