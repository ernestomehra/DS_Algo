# print a list in a wave, arr[0] > arr[1] < arr[2] >arr[3]

def wave_list(arr):
  sorted_list = sorted(arr)
  for i in range(0, len(arr), 2):
    sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]

  return sorted_list
