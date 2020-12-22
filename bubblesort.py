def bubblesort(arr):
  for passnum in range(len(arr)-1, 0, -1) #Outer loop to make sure pass repeats for all numbers.
    for i in range(passnum):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr
    
          

    
