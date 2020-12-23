def unorderedSearch(arr, searchElement):
  for i in range(0, len(arr)):
    if arr[i] == searchElement:
      return True
  return -1
