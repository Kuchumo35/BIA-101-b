# Binary Search


arr = [3,4,5,6,7,8,9]
target = 7
low = 0
high = len(arr) -1
#loop
result = False
#print('low', 'low')
while low <= high:
    mid = (low + high) // 2
   # print('mid:', mid)
    #print('low:', mid)
    #print('high:', mid)
    #print('-----')
    #compare the middle with the target
    if arr[mid] == target:
        print('found')
        break
    if target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1
print('not found')
