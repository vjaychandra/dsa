
def search_2D(matrix, target):

    for row in matrix:
        if row[0] <= target <= row[-1]:
            return search(row, target)


def search(array, target):

    l, r = 0, len(array)-1

    while l <= r:
        mid = (l+r) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3

print(search_2D(matrix, target))
            
