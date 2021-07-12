import re
import sys
def PowerSet(brackets,visited,result):
    if len(brackets) == 0:
        if len(visited) != 0:
            result.append(visited)
        return
    include = visited + list(brackets[0])
    PowerSet(brackets[1:],visited,result)
    PowerSet(brackets[1:],include,result)
    
if __name__ == '__main__':
    expression = sys.stdin.readline().strip()
    openBrackets = []
    bracketsPair = []
    for i,v in enumerate(expression):
        if v == '(':openBrackets.append(i)
        if v == ')':bracketsPair.append((openBrackets.pop(),i))
    result = []
    PowerSet(bracketsPair,[],result)
    ans = set()
    for row in result:
        s = list(expression[:])
        for index,char in enumerate(expression):
            if index in row: 
               s[index] = ''
        ans.add(''.join(s))
    for i in sorted(ans): print(i)


