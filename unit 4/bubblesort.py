input_arr = [6,3,1,5,0]
def bubble_sort(arr):
  n = len(arr)
  for i in range(n): # 0,1,2,3,4,5
    for k in range(0, n):
      elementright = arr[k]
      elementleft = arr[k+1]
      print('elementright:', elementright)
      print('elementleft:', elementleft)
      print('================================')
