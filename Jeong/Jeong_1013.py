import re
pattern = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    s = input()
    if re.fullmatch(pattern,s):
        print('YES')
    else:
        print('NO')