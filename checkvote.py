userInput = input('please type your age:')
userAge = int(userInput)
if userAge <= 18:
    print('You cannot vote')
else:
    print('you can vote')