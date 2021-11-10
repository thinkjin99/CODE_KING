import copy
n,m = input().split()
def Permutation(arr,path):
    res = ''
    if(len(path) == int(m)): 
        for i in path:
            res += f"{i} "
        print(res)
        return 
    #중복된 요소를 제거해야하기에 set으로 범위를 생성해 중복을 제거한다.
    for i in sorted(set(arr)): 
        # if _path and _path[-1] > i: continue
        index  = arr.index(i)
        Permutation(arr[:index] + arr[index + 1:], path + [i])

if __name__ =='__main__':
    Permutation([int(i) for i in input().split()],[])