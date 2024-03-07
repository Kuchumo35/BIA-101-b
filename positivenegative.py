# objective
# create a program that takes in user input
# and determines if the number is positive or negative
# print: "Your number is positive" or "Your number is negative"

# If else
# print()
# input()


userInput = input('Please type any number: ')


userInputNumber = int(userInput)
print('The type of userInputNumber is:', type(userInputNumber))

if userInputNumber > 0:
    print('The number is positive')
elif userInputNumber < 0:
    print('The number is negative')
elif userInputNumber == 0:
    print('The number is zero')


