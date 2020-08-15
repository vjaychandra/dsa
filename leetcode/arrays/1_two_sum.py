nums = [2, 7, 11, 15]
target = 9

num_dict = {}

def two_sum(nums, target):

    for index, num in enumerate(nums):

        diff = target - num
        
        if diff not in num_dict:
            num_dict[num] = index
        else:
            return [num_dict[diff], index]

print(two_sum(nums, target))
        


