matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if r != c and r < c:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    matrix[r] = matrix[r][::-1]

print(matrix)
