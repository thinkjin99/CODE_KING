import sys
def getPrioNum(words):
    weightDict = dict() #각 알파벳 별 가질 수 있는 최대 잠재 값을 구한다.
    for word in words:
        digit = len(word) - 1
        for character in word:
            if character in weightDict:
                weightDict[character] += pow(10,digit) #첫 번쨰 알파벳의 잠재 값을 구한다. 
            else: weightDict[character] = pow(10,digit)
            digit -= 1
    for i,(k,v) in enumerate(sorted(weightDict.items(),key = lambda x : x[1], reverse = True)):
        weightDict[k] = 9 - i
    return weightDict

if __name__ == '__main__':
    n = int(input())
    priorityQueue = []
    words = []
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        words.append(word)
    valueDict = getPrioNum(words)
    # print(valueDict)
    result = 0
    for word in words:
        digit = len(word) - 1
        for character in word:
            result += valueDict[character] * pow(10,digit)
            digit -= 1
    print(result)
    

