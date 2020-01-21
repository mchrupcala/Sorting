# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # print(arr)
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    # print(arr)
    return arr






# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # print(arr)
    copy = arr.copy()
    temp = 0
    swap = 1
    while swap > 0:
        for x in range(len(arr)):
            if arr[x] != arr[-1] and arr[x] > arr[x+1]:
                temp = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = temp
        if arr == copy:
            swap = 0
        else:
            copy = arr.copy()
    # print(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr