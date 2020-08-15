t = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

i, j = 0, 0
indexes = []

for row in range(len(t)):
    for col in range(len(t[row])):
        if t[row][col] == 0:
            indexes.append([row, col])
            
for item in indexes:
    row, col = item
    t[row] = [0] * len(t[row])
    for i in range(len(t)):
        t[i][col] = 0
