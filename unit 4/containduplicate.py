input_arr = [1,2,3,4]

def containsDuplicate(nums):
    for element in nums:
        for i in nums:
            print('element:', element)
            print('i', i)
            print('====================')
    return True
    
    
    # either return true or false
result = containsDuplicate(input_arr)
print(result)