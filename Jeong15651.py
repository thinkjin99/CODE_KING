import copy
n,m = input().split()
def Permutation(arr,path):
    if(len(path) == int(m)): 
        for i in path:
            print(str(i) + " ",end = '')
        print()
        return

    #왜 그냥 path를 사용하면 안될까..?
    _path = copy.deepcopy(path)
    for i in arr:
        _path.append(i)
        Permutation(arr,_path)
        _path = _path[:-1]
        #_path.remove??

if __name__ =='__main__':
    Permutation([i for i in range(1,int(n) + 1)],[])