nums = [0,1,0,3,12]


# idea is to count the non zero and add them from beginning
# add 0 as equal to the count starting from count index

# also count the zero's and pop them from their index
# add zeros to the last as per the count

count = 0

for num in nums:
    if num != 0:
        nums[count] = num
        count += 1

while count < len(nums):
    nums[count] = 0
    count += 1

print(nums)
