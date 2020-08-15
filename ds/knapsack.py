w = [1, 3, 5, 2, 6]
v = [9, 6, 4, 5, 2]
W = 15

v = [60, 100, 120]
w = [10, 20, 30]
W = 50
n = len(v)

# recursive
def knapsack(w, v, W, n):

    if n == 0 or W == 0:
        return 0
        
    if w[n-1] > W:
        return knapsack(w, v, W, n-1)
    else:
        return max(v[n-1] + knapsack(w, v, W-w[n-1], n-1), knapsack(w, v, W, n-1))


# iterative - bottom up approach
def knapsack(wt, vl, W, n):

    M = [[0 for i in range(W+1)] for j in range(n+1)]

    # v/i -> n, w/j -> W

    for v in range(1, n+1):
        for w in range(1, W+1):
            if wt[v-1] <= w:
                M[v][w] = max(vl[v-1] + M[v-1][w-wt[v-1]], M[v-1][w])
            else:
                M[v][w] = M[v-1][w]

    return M[n][w]


#print(knapsack(w, v, W, n))



def subset_sum(arr, target):

    M = [[False for _ in range(target+1)] for _ in range(len(arr)+1)]

    for j in range(target+1):
        M[0][j] = False
    for i in range(len(arr)+1):
        M[i][0] = True

    for i in range(1, len(arr)+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                M[i][j] = M[i-1][j-arr[i-1]] or M[i-1][j]
            else:
                M[i][j] = M[i-1][j]

    print(M[len(arr)][target])


def equal_sum_subset(arr):

    arr_sum = sum(arr)

    if arr_sum%2 != 0:
        return False

    equal_halves = int(arr_sum/2)
    subset_sum(arr, equal_halves)


def subsets_count(arr, target):

    M = [[0 for _ in range(target+1)] for _ in range(len(arr)+1)]

    for j in range(target+1):
        M[0][j] = 0
    for i in range(len(arr)+1):
        M[i][0] = 1

    for i in range(1, len(arr)+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                M[i][j] = M[i-1][j-arr[i-1]] + M[i-1][j]
            else:
                M[i][j] = M[i-1][j]

    print(M[len(arr)][target])


arr = [1, 5, 11, 5]
target = 11
#subset_sum(arr, target)
#equal_sum_subset(arr)
#subsets_count(arr, target)

                
















