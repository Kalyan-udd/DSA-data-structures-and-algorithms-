def division_of_array(nums):
    n = len(nums)
    total_sum = float('inf')
    if n<=3:
        return sum(nums)
    for i in range(1,n-1):
        for j in range(i+1,n):
            cost = nums[i]+nums[j]
            total_sum = min(total_sum,cost)
    total_sum += nums[0]
    return total_sum

def division_of_array_1(nums):
    rest = nums[1:]
    rest = sorted(rest)
    return nums[0]+rest[0]+rest[1]

