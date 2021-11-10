import copy
n,m = tuple(map(int,input().split()))
def Permutation(arr,depth):
    if depth == m: 
        res = ''
        cur = 0
        for i in arr[:m]:
            if i < cur: return #작은 값만 출력해줘야 한다.
            else:
                res += f"{i} "
                cur = i
        print(res)
        return

    needSwap = copy.deepcopy(arr[depth:]) #이미 정렬한 요소는 교환 대상에서 배제한다.
    for i in arr[depth : n]:
        #작은 순으로 출력을 해줘야 하므로 함으로 최소값과 우선 교환해준다
        index = arr.index(min(needSwap))
        arr[depth],arr[index] = arr[index],arr[depth]
        #교환한 최소 값은 제거해줘야 하므로 삭제해준다.
        needSwap.remove(min(needSwap))
        Permutation(arr,depth + 1)
        arr[depth],arr[index] = arr[index],arr[depth]

if __name__ =='__main__':
    Permutation([int(i) for i in input().split()],0)