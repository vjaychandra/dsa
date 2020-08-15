x = -123
op = 0

if x < 0:
    sign = -1
else:
    sign = 1

x = abs(x)
while x > 0:
    op = op*10 + (x%10)
    x = int(x/10)
op = sign*op

if op in range(-2**31, (2**31)-1):
    print(-1)

print(sign*op)
