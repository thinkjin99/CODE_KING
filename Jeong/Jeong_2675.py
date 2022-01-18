for _ in range(int(input())):
    n,s = input().split()
    print(''.join([int(n) * c for c in s]))