def orderedSearch(arr, element):
  sortedlist = sorted(arr)
  for i in (0, len(arr)):
    if arr[i] == element:
      return True
    elif arr[i] > element:
      return False
  
  
