def coun_dominant_indices(nums):
    n = len(nums)
    if n==0:
        return 0
    
    j = 1
    average = nums[n-1]
    count = 0
    i = n-1
    while i >= 0:
        if nums[i] > average:
            count += 1
        i -= 1
        average = ((average*j)+nums[i])/(j+1)
        j+=1
    return count


def MergeAdjacentEqualElements(nums: list[int]):
    n = len(nums)
    i = 0
    while i<=n-2:
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums.pop(i+1)
            n = len(nums)
            print(nums)
            MergeAdjacentEqualElements(nums)
        else:
            i+=1    
    return nums



print(MergeAdjacentEqualElements(nums = [1,2,2,4,1]))