# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)-1):
          if arr[smallest_index] > arr[j + 1]:
            smallest_index = j + 1
            
        arr[cur_index], arr[smallest_index] \
        = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
  while True:
      swap_times = 0
      for i in range(0, len(arr)-1):
          if arr[i] > arr[i + 1]:
              arr[i + 1], arr[i] = arr[i], arr[i + 1]
              swap_times += 1
      if swap_times == 0:
        break
  return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if all(i >= 0 for i in arr):
        unique = list(range(max(arr, default=0)+1))
        dict_a = {unique[i]: arr.count(unique[i]) for i in unique}
        output = [x for t in dict_a for x in [t]*dict_a[t]]
    else:
        output = 'Error, negative numbers not allowed in Count Sort'

    return output