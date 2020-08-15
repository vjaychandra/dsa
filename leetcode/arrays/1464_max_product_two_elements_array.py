# find the maximum value with two numbers in an array
# idea is to find the two max values as the product of them is the output


def maxProduct(nums):

    v1, v2 = 0, 0

    for num in nums:
        if num > v1:    # current greater than max
            v2 = v1     # assign max to second max
            v1 = num    # update the max value with current
        elif num > v2:
            v2 = num    # update the second max value with current
            
    return (v1-1) * (v2-1)

nums = [3,4,5,2]
print(maxProduct(nums))
