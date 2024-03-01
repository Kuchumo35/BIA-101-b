#Objective: a calculator application
# variables and if statement

#steps
#1. get input from the user
#2. do calculation based on user input
#3. give output to the user

print('*')
print('+')
print('-')
print('/')

whatusertyped = input()

print('user typed:', whatusertyped)
print('user input-type', type(whatusertyped))

print('-------------')
if whatusertyped == "+":
    print('Doing Addition')

print('doing more addition')

if whatusertyped == "-":
    print('doing subtraction')
    print ('doing more subtraction')

if whatusertyped == "*":
    print('doing multiplication')
    print('doing more multiplication')



