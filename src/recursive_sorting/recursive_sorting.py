# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(len(merged_arr)):
      if len(arrA) != 0 and len(arrB) != 0:
          if arrA[0] <= arrB[0]:
              merged_arr[i] = arrA[0]
              arrA = arrA[1:]
          else:
              merged_arr[i] = arrB[0]
              arrB = arrB[1:]
      else:
        merged_arr[i:] = max(arrA, arrB, key=len)
        break
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base case
    if len(arr) <= 1:
        return arr

    # recursive case
    else:
        arr1 = arr[:len(arr)//2]
        arr2 = arr[len(arr)//2:]
        return merge(merge_sort(arr1), merge_sort(arr2))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
