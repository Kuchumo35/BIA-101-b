# searching 
# sorting

#input 
user_input = [1,2,3,5,6,7,8,9,10,11]

# check if certain number exist in user input

n = 12
result = False

for i in user_input:
    if i == n:
        result = True

if result == True:
    print('Found')

else:
    print('Not found')

# time complexity
print('---Time and Space Complexity---') 
print('Break')
input= [1,2,3,4,5]
for i  in input:
    print('hi')
    if i == 1:
        break
print('continue')
input= [1,2,3,4,5]
for i  in input:
    
    if i == 1:
        continue
    print('hi')




   