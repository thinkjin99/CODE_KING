n,m = tuple(map(int,input().split()))
def Permutation(arr,depth):
    if depth == m: 
        res = ''
        cur = 0 
        for i in arr[:m]:
            if cur > i: return
            res += f"{i} "
            cur = i
        print(res)
        return
    for i in range(depth, n):
        #상태 트리를 생각하면 단순하다. 각각의 숫자의 위치를 교환하는 것이다.
        arr[depth],arr[i] = arr[i],arr[depth]
        Permutation(arr,depth + 1)
        #위치를 바꾼 배열을 원 상태로 복기 시킨다
        arr[depth],arr[i] = arr[i],arr[depth]


if __name__ =='__main__':
    Permutation([i for i in range(1,n + 1)],0)