import sys
input = sys.stdin.readline
n = int(input())
res = 0 << 20
for _ in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        cmd, value = cmd[0], int(cmd[1]) - 1
    else:
        if cmd[0] == 'all':
            res  = res | ~res
        elif cmd[0] == 'empty':
            res = res & 0 
    if cmd == 'add':
        res = res | 1 << value
    elif cmd == 'check':
        if res & (1 << value):
            print(1)
        else: print(0)
    elif cmd == 'remove':
        res = res & ~(res << value)
    elif cmd == 'toggle':
        res = res ^ (1 << value)