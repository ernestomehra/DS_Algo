
def selection_sort(arr):

  for i in range(len(arr)-1):
    minimum_value = min(arr[i:])
    index_min = i + arr.index(minimum_value)
    if arr[i] > minimum_value:
      arr[i], arr[index_min] = arr[index_min], arr[i]
      
  return arr
