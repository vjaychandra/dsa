wt = [1, 2, 4, 6]
vl = [5, 3, 5, 6]
W = 30
n = len(vl)

def knapsack(wt, vl, W, n):

    M = [[0 for i in range(W+1)] for j in range(n+1)]

    for v in range(1, n+1):
        for w in range(1, W+1):
            if wt[v-1] <= w:
                M[v][w] = max(vl[v-1] + M[v-1][w-wt[v-1]], M[v-1][w])
            else:
                M[v][w] = M[v-1][w]
    return M[n][w]

max_profit = knapsack(wt, vl, W, n)
