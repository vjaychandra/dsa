def partition(array, start, end):

    pos = start

    for i in range(start, end):
        if array[i] < array[end]:
            array[pos], array[i] = array[i], array[pos]
            pos += 1
    array[pos], array[end] = array[end], array[pos]
    return pos


def quick_sort(array, start, end):

    if start < end:
        pos = partition(array, start, end)
        quick_sort(array, start, pos-1)
        quick_sort(array, pos+1, end)

    

if __name__ == "__main__":

    array = [3,2,3,1,2,4,5,5,6]
    quick_sort(array, 0, len(array)-1)
    print("SortedArray: ", array)
