"""
P: To find the non repetitive element in an array

-> We can do bby using XOR operation on each element because

XOR -> on same element is ZERO
XOR -> any element with 0 is same element

"""


nums = [4,1,2,1,2]

res = 0

for num in nums:
    res ^= num

print(res) # returns the distinct element in the array

