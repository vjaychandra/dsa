
def rotate(nums, k):

    k = k % len(nums)

    if k:
        nums[:k], nums[-k:] = nums[-k:], nums[:k]
    return nums



if __name__ == "__main__":

    nums = [1,2,3,4,5,6,7]
    k = 3

    nums = [-1,-100,3,99]
    k = 2

    print(rotate(nums, k))


