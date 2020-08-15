
def myAtoi(s):

    s = s.strip().split()
    s = s[0]

    op = 0
    i, j = 0, 0
    
    if 97 < ord(s[i].lower()) < 123:
        return 0    

    if s[0] in ['-', '+']:
        s = s[1:]
        sign = s[0]
    else:
        sign = 1

    while i < len(s) and s[i].isdigit():
        op = op*10 + (ord(s[i])-ord('0'))
        i += 1

    return max(-2**31, min(sign*op, 2**31-1))


print(myAtoi("-91283472332"))
#print(myAtoi("-42"))


