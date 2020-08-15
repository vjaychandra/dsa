count = 0
for index in range(1, 1000):
    if index%3==0 or index%5==0:
        count += index
print(count)        
