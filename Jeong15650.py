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
        arr[depth],arr[i] = arr[i],arr[depth]
        Permutation(arr,depth + 1)
        arr[depth],arr[i] = arr[i],arr[depth]


if __name__ =='__main__':
    Permutation([i for i in range(1,n + 1)],0)