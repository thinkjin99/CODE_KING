n = input()
a = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()],reverse = True)
res = 0
#zip사용 법
#zip은 여러개의 이터레이터를 인자로 받고 각 원소를 튜플 형태로 만들어 반환해준다.
for i,j in zip(a,b):
    res += i * j
print(res)

