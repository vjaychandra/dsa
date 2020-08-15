nums = [1,2,3,1]

nd = {}

for num in nums:
    if not nd.get(num):
        nd[num] = 1
    else:
        nd[num] += 1

    if nd[num] > 1:
        break
