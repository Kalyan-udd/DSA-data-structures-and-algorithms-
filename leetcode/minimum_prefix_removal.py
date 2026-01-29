def minimum_prefix_removal(nums):
    n = len(nums)
    i = n-1
    while i>0:
        if nums[i]<=nums[i-1]:
            return i
        i-=1

print(minimum_prefix_removal([1,-1,2,3,3,4,5]))

def rotate_non_negative(nums,k):
    n = len(nums)
    indices = []
    values = []
    for i in range(n):
        if nums[i]>=0:
            indices.append(i)
            values.append(nums[i])
    m = len(indices)
    if m>1:
        p = k%m
        temp = values[0:p]
        for i in range(p,n):
            values[i-p] = values[i]
        for i in range(n-p,n):
            values[i] = temp[i-n+p]
        for i in range(m):
            nums[indices[i]] = values[i]
    return nums


