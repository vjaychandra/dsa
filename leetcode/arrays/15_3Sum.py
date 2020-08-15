
def threeSum(nums):

    result = []
    for i in range(len(nums)-1):
        s = set()
        for j in range(i+1, len(nums)):
            x = -(nums[i] + nums[j])
            if x in s:
                items = sorted([x, nums[i], nums[j]])
                if items not  in result:
                    result.append(items)
            else:
                s.add(nums[j])
    return result

                      

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
