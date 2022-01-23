import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = [int(i) for i in input().split()]
stack = [arr[-1]] #오른쪽에 위치한 수를 저장한다.
res = []
for i in reversed(range(n-1)): #뒤에서 부터 검사한다.
    while stack:
        if stack[-1] <= arr[i]: #스텍에 자신보다 큰 요소가 등장할 때 까지 제거한다.
            stack.pop()
        else: break
    #스텍은 비었거나 i번째의 오큰수가 저장돼 있다. 
    res.append(stack[-1] if stack else -1)
    #스텍에 i번째 요소를 추가해준다.
    stack.append(arr[i])
for i in reversed(res):
    print(i, end = ' ')
#마지막은 항상 -1이다.
print(-1,end=' ')