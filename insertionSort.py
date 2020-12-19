
def insertionsort(arr):
  for i in range (1, len(arr)):
    temp = arr[i] 
    k = i
    while  k > 0 and temp < arr[k-1]:
      arr[k] = arr[k-1]
      k -= 1
    arr[k] = temp
  return arr



def insertionsort1(arr):
  for i in range (1, len(arr)):
    temp = arr[i]
    k = i - 1
    while k > 0 and temp < arr[k]:
      arr[k+1] = arr[k]
      k -= 1
    arr[k+1] = temp 
  return arr 
