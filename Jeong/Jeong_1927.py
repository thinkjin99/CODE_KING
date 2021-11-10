import sys
class Node:
    def __init__(self,num):
        self.original = num
        self.absNum = abs(num)

class Minheap:
    def __init__(self):
        self.__heapSize = 0
        self.heap = [0 for _ in range(100001)]

    def heapPush(self,num):
        self.__heapSize += 1
        index = self.__heapSize
        self.heap[index] = Node(num)
        while index > 1:
            if self.heap[index].absNum < self.heap[index//2].absNum:  
                self.heap[index],self.heap[index//2] = self.heap[index//2],self.heap[index]
                index = index // 2
            elif self.heap[index].absNum == self.heap[index//2].absNum:
                if self.heap[index].original < self.heap[index//2].original:
                    self.heap[index],self.heap[index//2] = self.heap[index//2],self.heap[index]
                    index = index // 2
                else: break
            else: break
    
    def Heapify(self):
        index = 1
        while index <= self.__heapSize//2:
            child = index * 2 if self.heap[index * 2].absNum < self.heap[index * 2 + 1].absNum else index * 2 + 1
            if self.heap[index * 2].absNum  == self.heap[index * 2 + 1].absNum:
                child = index * 2 if self.heap[index * 2].original < self.heap[index * 2 + 1].original else index *2 + 1

            if self.heap[index].absNum > self.heap[child].absNum:
                self.heap[index],self.heap[child] = self.heap[child],self.heap[index]               
                index = child
        
            elif self.heap[index].absNum == self.heap[child].absNum:
                if self.heap[index].original > self.heap[child].original:
                    self.heap[index],self.heap[child] = self.heap[child],self.heap[index]
                    index = child
                else: break
            else: break    

    def heapPop(self):
        if self.__heapSize > 0:
            extractMin = self.heap[1].original
            self.heap[self.__heapSize],self.heap[1] = self.heap[1],self.heap[self.__heapSize]
            self.heap[self.__heapSize] = Node(pow(2,31))
            self.__heapSize -= 1
            self.Heapify()
            return extractMin
        return 0

if __name__ == '__main__':
    maxHeap = Minheap()
    res = []
    for _ in range(int(input())):
        num = int(sys.stdin.readline())
        if num == 0:
            res.append(maxHeap.heapPop())
        else: maxHeap.heapPush(num)
    for i in res:
        print(i)

