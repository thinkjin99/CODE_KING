import sys
class Node:
    def __init__(self,num = None):
        self.num = num
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self,num):
        self.head = Node(num)

    def Push(self,num):
        loc = self.head
        while True:
            if loc.num > num:
                if loc.left != None:
                    loc = loc.left
                else:
                    loc.left = Node(num)
                    break
            else:
                if loc.right != None:
                    loc = loc.right
                else:
                    loc.right = Node(num)
                    break

def PostOrder(node):
    if node != None:
        PostOrder(node.left)
        PostOrder(node.right)
        print(node.num)

if __name__ == '__main__':
    sys.setrecursionlimit(20_000)
    Bst = BinarySearchTree(int(sys.stdin.readline()))
    while True:
        try:
            num = int(sys.stdin.readline())
            Bst.Push(num)
        except:
            break
    PostOrder(Bst.head)