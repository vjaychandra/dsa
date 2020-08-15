def lcsubstring(X, Y):

    result = 0

    n, m = len(X), len(Y)
    t = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                t[i+1][j+1] = 1 + t[i][j]
                result = max(result, t[i+1][j+1])
            else:
                t[i+1][j+1] = 0

    return result

print(lcsubstring("abcde", "abc"))
