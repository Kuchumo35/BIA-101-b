 # creation of array
print('only array')
array1 = [1,2,3, "thimphu", 2.5]
print(array1)

# retrieving
print('retrieving element')
element1 = array1[0]
element2 = array1[4]
lastelement = array1[-1]

print(element1)
print(element2)
print(lastelement)

#modifying element
print('changing array value')
array1[0] = 10
print(array1)

# getting number of elements in an array
print('length of array')
no_of_elements = len(array1)
print(no_of_elements)

# slicing
print('selecting more than 1 elements')
elements = array1[0:3]
print(elements)

# lists
print('new list')
array1 = [1,2]
array2 = ['thimphu','wangdue']
new_array = array1 + array2
print(new_array)

# t or f
print('checking whether the elements are there')
array1 = [1,2]
array2 = ['thimphu','wangdue']
find_array = 2
new_array = find_array in array1
print(new_array)

# adding variable 
print('appending')
array1 = [1,2]
array1.append(7)
print(array1)

# insert
print('inserting elements')
array1 = [1,2]
array1.insert(1,6)
print(array1)

# Sort the list
print('sorting')
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers) 

# Creating a stack
print('stacks')
stack = []
# Push (add) elements to the stack
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
