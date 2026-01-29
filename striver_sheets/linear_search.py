def linear_search(nums, num):
    n = len(nums)
    for i in range(n):
        if nums[i] == num:
            return i
    else:
        return -1
    
print(linear_search(nums= [1,67,2,9,3,8,5,4,9,3,2], num = 10))