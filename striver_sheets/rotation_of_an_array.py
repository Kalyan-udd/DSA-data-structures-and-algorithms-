def rotation_of_an_array(nums):
    n = len(nums)
    temp = nums[0]
    for i in range(n-1):
        nums[i] = nums[i+1]
    nums[n-1] = temp
    return nums

print(rotation_of_an_array(nums = [1,2,3,4,5,6]))