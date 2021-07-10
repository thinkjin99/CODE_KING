import sys
class Node:
    def __init__(self,key,data = None):
        self.key = key
        self.data = data
        self.child = {}
class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self,PhoneNum):
        current = self.head
        for n in PhoneNum:
            if n not in current.child:
                current.child[n] = Node(n)
            current = current.child[n]
        current.data = True

    def search(self,PhoneNum):
        current = self.head
        for n in PhoneNum: #접두사니까 자기자신보다 한칸 작은 글자까지 확인한다.
            if current.data != None:
                return True
            current = current.child[n]
        return False #trie안에 문자열이 존재
        #trie안에 문자열이 존재하지 않음

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(sys.stdin.readline())
        trie = Trie()
        phoneNums = []

        for _ in range(n):
            pNum = sys.stdin.readline().strip()
            phoneNums.append(pNum)
            trie.insert(pNum)

        is_prefix = False
        for pNum in phoneNums:
            if trie.search(pNum) == True:
                is_prefix = True
                break
    
        if is_prefix: print("NO")
        else: print('YES')