s = input()
stack = []
length = 0
k  = ''
for c in s:
    if c.isdigit():
        length += 1
        k = c
    elif c == '(':
        stack.append((k,length-1))
        length = 0
    else:
        k,left = stack.pop()
        length = (int(k) * length) + left

print(length)