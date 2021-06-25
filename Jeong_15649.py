n,m = input().split()
def Permutation(arr,path):
    if(len(path) == int(m)): 
        res = ''
        for i in path:
            res += f"{i} "
        print(res)
        return

    for i in range(len(arr)):
        Permutation(arr[:i] + arr[i + 1:], path + [arr[i]])

if __name__ =='__main__':
    Permutation([i for i in range(1,int(n) + 1)],[])