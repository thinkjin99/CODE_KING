import copy
n,m = input().split()
def Permutation(arr,path):
    if(len(path) == int(m)): 
        for i in path:
            print(str(i) + " ",end = '')
        print()
        return

    #왜 그냥 path를 사용하면 안될까..?
    #append를 하면서 필연적으로 path 자체의 값이 변하게 돼 있다.
    #호출한 위치를 정확히 기억하기 위해서 copy를 사용한다.
    #예를들어 11에서 순회 했을 때 호출되는 path들은 111,112,113이고 이대로 함수를 종료하면
    # 11로 돌아가게 된다. 11로 돌아가면 또다시 111,112,113을 출력하게 되기에 path가 1로 돌아가게 하기 위해서
    #copy를 따로 만들어 사용한다. 매개변수 path를 그대로 사용하면 호출 부를 정확히 파악 할 수 없다.
    _path = copy.deepcopy(path)
    for i in arr:
        if _path and _path[-1] > i: continue
        _path.append(i)
        Permutation(arr,_path)
        _path = _path[:-1]
        # print(_path)
        #remove를 사용하면 안되는 이유는 remove는 for문을 돌면서 실행하면 리스트 자체에 손실이 생기며
        #삭제에 누락이 발생할 수도 있다.
        #_path.remove??

if __name__ =='__main__':
    Permutation([i for i in range(1,int(n) + 1)],[])