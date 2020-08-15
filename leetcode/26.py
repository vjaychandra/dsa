def removeDuplicates(nums):

    i = 0
    for index in range(1, len(nums)):
        if nums[index] != nums[i]:
            i += 1
            nums[i] = nums[index]
    return i + 1
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
