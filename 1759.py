n,m = input().split()
def Permutation(arr,path):
    if(len(path) == int(n)):
        moumCnt = 0
        for i in 'aeiou':
            moumCnt += path.count(i)
        if len(path) - moumCnt > 1 and moumCnt > 0:
            res = ''
            for i in path:
                res += i
            print(res)
        return
    for i in arr:
        index = arr.index(i)
        if path and path[-1] > i: continue
        Permutation(arr[:index] + arr[index + 1:],path + [i])


if __name__ =='__main__':
    Permutation(sorted([i for i in input().split()]),[])
