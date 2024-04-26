

input_str = '(((())))'
stack = []
for i in input_str:
    if i == '(':
        stack.append(i)

    if i == ')':
        stack.pop()
length = len(stack)
if length == 0:
    print(True)

else:
    print(False)


    
       
    


