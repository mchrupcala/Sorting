# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    temp = []
    print("arrA: ", arrA, "arrB: ", arrB)
    temp = arrA + arrB
    temp.sort()
    # if arrA < arrB:
    #     merged_arr = arrA + arrB
    # elif arrB < arrA:
    #     merged_arr = arrB + arrA
    # TO-DO
    
    return temp


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # print(arr)
    # TO-DO
    # lower = 0
    # upper = len(arr)
    i = len(arr)//2
    if len(arr) <= 1:
        return arr
    else:
        arr1 = arr[:i]
        arr2 = arr[i:]
        m1 = merge_sort(arr1)
        m2 = merge_sort(arr2)
        return merge(m1, m2)
    # while len(arr) > 1:
    #     arr1 = arr[lower:i]
    #     arr2 = arr[i:upper]
    #     merge_sort(arr1)
    #     merge_sort(arr2)
    #     arr = arr1 + arr2
    # return arr


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
