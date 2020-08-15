"""
-> Create new array based in the index array indexes
"""

def createTargetArray(nums, index):

    output = []

    ptr = 0

    while ptr < len(index):
        output = output[:index[ptr]] + [nums[ptr]] + output[index[ptr]:]
        ptr += 1
    return output


nums = [4,2,4,3,2]
index = [0,0,1,3,1]
print(createTargetArray(nums, index))
