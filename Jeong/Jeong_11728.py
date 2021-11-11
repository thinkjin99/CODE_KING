def merge(A,B):
    c = []
    indexA,indexB = (0,0)
    while indexA < len(A) and indexB < len(B):
        if A[indexA] < B[indexB]:
            c.append(A[indexA])
            indexA += 1
        else:
            c.append(B[indexB])
            indexB += 1
    if indexA == len(A):
        c.extend(B[indexB:])
    else:
        c.extend(A[indexA:])
    return c


if __name__ == '__main__':
    n,m = input().split()
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    res = ''
    for i in merge(a,b):
        res += f"{i} "
    print(res)
