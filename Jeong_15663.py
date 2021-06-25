import copy
n,m = input().split()
def Permutation(arr,path):
    if(len(path) == int(m)): 
        for i in path:
            print(str(i) + " ",end = '')
        print()
        return 

    for i in sorted(set(arr)): #중복된 요소를 제거해야하기에 set으로 범위를 생성해 중복을 제거한다.
        arrCopy = copy.deepcopy(arr)
        _path = copy.deepcopy(path)
        # if _path and _path[-1] > i: continue
        _path.append(i)
        arrCopy.remove(i)
        Permutation(arr,_path)

if __name__ =='__main__':
    Permutation([int(i) for i in input().split()],[])