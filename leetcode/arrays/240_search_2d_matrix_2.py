m = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

search = 5


def search_matrix(matrix, target):
    for row in matrix:
        if row[0] > target or row[-1] < target:
            continue

        l, r = 0, len(row)-1
        while l <= r:
            mid = (l+r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
    return False

print(search_matrix(m, search))
