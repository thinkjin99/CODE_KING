import sys
class MaxHeap:
    def __init__(self):
        self.__heapSize = 0
        self.heap = [0 for _ in range(100001)]
    
    def heapPush(self,num):
        self.__heapSize += 1
        index = self.__heapSize
        self.heap[index] = num
        while index > 1 and num > self.heap[index//2]:
            self.heap[index],self.heap[index//2] = self.heap[index//2],self.heap[index]
            index = index // 2
        return
    
    def Heapify(self):
        index = 1
        while index <= self.__heapSize//2:
            child = index * 2 if self.heap[index * 2] > self.heap[index * 2 + 1] else index * 2 + 1
            if self.heap[index] < self.heap[child]:
                self.heap[index],self.heap[child] = self.heap[child],self.heap[index]
                index = child
            else: break
                
    def heapPop(self):
        if self.__heapSize > 0:
            self.heap[self.__heapSize],self.heap[1] = self.heap[1],self.heap[self.__heapSize]
            extractMax = self.heap[self.__heapSize]
            self.heap[self.__heapSize] = 0
            self.__heapSize -= 1
            self.Heapify()
            print(extractMax)
        else: print(0)

if __name__ == '__main__':
    maxHeap = MaxHeap()
    for _ in range(int(input())):
        num = int(sys.stdin.readline())
        if num == 0:
            maxHeap.heapPop()
        else: maxHeap.heapPush(num)


