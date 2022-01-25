for _ in range(int(input())):
    h,_,n = map(int,input().split())
    print(str((n - 1) % h + 1) + str((n - 1) // h + 1 ).rjust(2,'0'))