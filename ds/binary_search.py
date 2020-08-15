def binary_search(array, item):

    if len(array)>0:

        mid = len(array)//2

        if item == array[mid]:
            return True

        if item > array[mid]:
            return binary_search(array[mid+1:], item)
        else:
            return binary_search(array[:mid], item)

    return False

if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 2))
