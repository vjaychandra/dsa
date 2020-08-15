
def arrange_coins(n):

    if n <= 1:
        return n

    i = 1
    while i < n:
        n -= i
        i += 1

    if n == i:
        return n
    else:
        return i-1
    

print(arrange_coins(10))

