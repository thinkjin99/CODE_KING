infix = input()
postfix = ''
operator = {'+' : 1, '-' : 1 ,'*' : 2 ,'/' : 2 ,'(' : -1, ')' : -1 }
stack = []
for s in infix:
    if s.isalpha():#if it's alpha just add to postfix
        postfix += s
    else:
        if not stack or s == '(': 
            stack.append(s) # when stack is empty or s is open brackets
            continue
        
        priority = operator[s]
        top_priority = operator[stack[-1]]
    	
        if priority > top_priority: #compare priority between stack top and s
            stack.append(s)

        else:
            while stack and priority <= top_priority:
                letter = stack.pop() #get recent operator
                if letter == '(': break
                if letter != ')':
                    postfix += letter
                top_priority = operator[stack[-1]] if stack else top_priority #update priority
            
            if s != ')': #append operator after pop
                stack.append(s)

postfix += ''.join(reversed(stack))
print(postfix)