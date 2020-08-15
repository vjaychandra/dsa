def runningSum(nums):
        
    output = 0
    for index, num in enumerate(nums):
        output += num
        nums[index] = output
    return nums


nums = [1,1,1,1,1]
print(runningSum(nums))
