def rotation_by_k_places(nums,k):
    n = len(nums)
    p = k%n
    for i in range(p):
        temp = nums[0]
        for i in range(n-1):
            nums[i] = nums[i+1]
        nums[n-1] = temp
    return nums

def rotation_by_k_places_2(nums, k):
    n = len(nums)
    p = k%n
    temp = nums[0:p]
    for i in range(p,n):
        nums[i-p] = nums[i]
    for i in range(n-p,n):
        nums[i] = temp[i-n+p]
    return nums

print(rotation_by_k_places_2(nums=[1,2,3,4,5], k = 64))
print(rotation_by_k_places(nums=[1,2,3,4,5], k = 64))