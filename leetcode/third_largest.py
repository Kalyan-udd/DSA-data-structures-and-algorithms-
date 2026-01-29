def third_largest(nums):
    nums = sorted(nums)
    n = len(nums)
    if n<3:
        return max(nums)
    return nums[-3]

print(third_largest(nums=[-1,2,3]))
    
    
    