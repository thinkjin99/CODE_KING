import sys
def BindNum(numList):
    binded = 0
    for i in range(0,len(numList) - 1,2):
        binded +=  numList[i] * numList[i + 1]
    if len(numList) % 2 != 0:
        binded += numList[-1]
    return binded
    
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    positives = []
    negatives = []
    ones = 0
    for _ in range(n):
        num = int(sys.stdin.readline())
        if num > 1:
            positives.append(num)
        elif num < 1:
            negatives.append(num)
        elif num == 1:
            ones += 1
    posBind = BindNum(sorted(positives,reverse = True))
    negBind = BindNum(sorted(negatives))
    print(posBind + negBind + ones)

