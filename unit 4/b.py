alien = 0
input_str = "(((("
for i in input_str:
    if i == "(":
        alien += 1
        
    else:
        alien =- 1
        

print('The final floor is:', alien)




