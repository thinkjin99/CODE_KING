import sys
def PreOrder(inOrder,postOrder,path):
    if len(inOrder) > 0:
        root = postOrder.pop()
        path.append(root)
        indexRoot = inOrder.index(root)
        PreOrder(inOrder[:indexRoot], postOrder[:indexRoot],path)
        PreOrder(inOrder[indexRoot + 1:], postOrder[indexRoot: indexRoot + len(inOrder[indexRoot + 1:])],path)
    return

n = int(input())
inOrder = list(map(int,sys.stdin.readline().split()))
postOrder = list(map(int,sys.stdin.readline().split()))
path = []
PreOrder(inOrder,postOrder,path)
res = ''
for p in path:
    res += f"{p} "
print(res.rstrip())