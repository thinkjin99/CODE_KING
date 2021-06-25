import copy
n,m = input().split()
def Permutation(arr,path):
    if(len(path) == int(m)): 
        for i in path:
            print(str(i) + " ",end = '')
        print()
        return 

    for i in sorted(set(arr)):
        arrCopy = copy.deepcopy(arr)
        _path = copy.deepcopy(path)
        _path.append(i)
        arrCopy.remove(i)
        Permutation(arrCopy,_path)


if __name__ =='__main__':
    Permutation([int(i) for i in input().split()],[])