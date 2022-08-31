def recursive_mod(k):
    if k <= 1:
        return a % c
    else:
        tmp = recursive_mod(k // 2)
        if k % 2 == 0: 
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

a, b, c = map(int, input().split())
res = recursive_mod(b)
print(res)