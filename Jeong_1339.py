import heapq
import sys
def getPrioNum(word):
    result = 0
    digit = len(word) - 1
    for c in word:
        if c == word[0]:
            result += pow(10,digit) #첫 번쨰 알파벳의 잠재 값을 구한다. 
        digit -= 1
    return result

def MakeQueue(priorityQueue):
    value = [i for i in range(9,-1,-1)] #0~9까지 알파벳의 값 생성
    valueDict = dict()
    while len(priorityQueue) > 0:
        longest = heapq.heappop(priorityQueue)[1]
        if longest[0] not in valueDict:
            valueDict[longest[0]] = value.pop(0)
        longest = longest[1:]
        if len(longest) > 0:
            heapq.heappush(priorityQueue,(-getPrioNum(longest),longest))
    return valueDict

if __name__ == '__main__':
    n = int(input())
    priorityQueue = []
    words = []
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        words.append(word)
        heapq.heappush(priorityQueue,(-getPrioNum(word),word))

    valueDict = MakeQueue(priorityQueue)
    print(valueDict)
    result = 0
    for word in words:
        digit = len(word) - 1
        for character in word:
            result += valueDict[character] * pow(10,digit)
            digit -= 1
    print(result)
    

