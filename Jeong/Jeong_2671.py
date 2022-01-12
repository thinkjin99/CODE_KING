import re
pattern = re.compile('(100+1+|01)+')
s = input()
if re.fullmatch(pattern,s):
    print('SUBMARINE')
else:
    print('NOISE')