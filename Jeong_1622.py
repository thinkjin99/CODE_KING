import sys
input = sys.stdin.readline
expression = input()
#2(3(4)25(6)1)
def find_brackets(expression):
    openBrackets = []
    bracketsPair = []
    for i,v in enumerate(expression):
        if v == '(':openBrackets.append(i)
        if v == ')':bracketsPair.append((openBrackets.pop(),i))
    
    return bracketsPair

def find_remains(start,end):
    e_range = expression[start + 1 : end + 1]
    last = []
    in_brackets = False
    for i, e in enumerate(e_range):
        if e == '(':
            in_brackets = True
        elif e == ')':
            in_brackets = False
            continue

        if in_brackets: continue

        if i+1 < len(e_range) and e_range[i+1] != '(': #k인 경우 검사
            last.append(e)
    return last

brackets = find_brackets(expression)
res,level_len = 0,0
while brackets:
    cur_s, cur_e = brackets.pop()
    k = expression[cur_s - 1]
    cur_len = cur_e - cur_s - 1
    level_len += cur_len * k

    next_s,next_e = brackets[0][0],brackets[0][1]
    if next_s < cur_s and next_e > cur_e:
        rest = find_remains(next_s,next_e)
        res = 
        level_len = 0


