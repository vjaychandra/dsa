def lcsubsequence(X, Y):

    n, m = len(X), len(Y)
    t = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                t[i+1][j+1] = 1 + t[i][j]
            else:
                t[i+1][j+1] = max(t[i+1][j], t[i][j+1])
    return t[-1][-1]


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


def printlcsubsequence(X, Y):

    n, m = len(X), len(Y)
    t = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                t[i+1][j+1] = 1 + t[i][j]
            else:
                t[i+1][j+1] = max(t[i+1][j], t[i][j+1])

    i, j = n, m
    output = ""

    print("\n".join(str(i) for i in t))

    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            output+= X[i-1]
            i -= 1
            j -= 1
        else:
            if t[i-1][j] > t[i][j-1]:
                i -= 1
            else:
                j -= 1

    print(output[::-1])
            

x = "ylqpejqbalahwr"
y = "yrkzavgdmdgtqpg"
#print(lcsubsequence(x, y))

x, y = "abcabcbb", "abcabcbb"[::-1]
#printlcsubsequence(x, y)
print(lcsubstring(x, y))

