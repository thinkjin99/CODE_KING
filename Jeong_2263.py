import sys
def PreOrder(inStart,inEnd,postStart,PostEnd,path):
    if inStart <= inEnd and postStart <= PostEnd:
        root = postOrder[PostEnd]
        path.append(str(root))
        indexRoot = indexes[root] #루트의 인덱스에 빠르게 접근
        leftSize = indexRoot - inStart #왼쪽 서브트리의 크기
        #루트를 기준으로 왼쪽과 오른쪽을 분할하고 전위 순회 합니다.
        PreOrder(inStart,indexRoot - 1,postStart,postStart + leftSize - 1,path)
        PreOrder(indexRoot + 1,inEnd,postStart + leftSize,PostEnd - 1,path)
        #post는 루트가 맨 뒤에 위치해 있으므로 맨 마지막 노드를 제거한다.
    return

n = int(input())
sys.setrecursionlimit(10000)
inOrder = list(map(int,sys.stdin.readline().split()))
postOrder = list(map(int,sys.stdin.readline().split()))
indexes = {} #각 원소 별 인덱스 저장
for i,v in enumerate(inOrder):
    indexes[v] = i
path = []
PreOrder(0,len(inOrder) - 1, 0, len(postOrder) - 1,path)
print(" ".join(path)) #join은 리스트 내부의 원소가 string이여야 사용가능하다.