# BRUTE CODE
def moving_zeroes(nums):
    n = len(nums)
    k = nums.count(0)
    non_zeroes = []
    for i in range(n):
        if nums[i] != 0:
            non_zeroes.append(nums[i])
    for i in range(n-k):
        nums[i] = non_zeroes[i]
    for i in range(k):
        nums[n-k+i] = 0 
    return nums

# BETTER / OPTIMAL CODE
def moving_zeroes_2(nums):
    n = len(nums)
    j = 0
    i = 1
    while i <n:
        if nums[j] == 0 and nums[i] == 0:
            i+=1
        elif nums[j] == 0 and nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j+=1
            i+=1
        elif nums[j] != 0:
            j+=1
            i+=1
    return nums

print(moving_zeroes(nums=[0,0,2,46,78,0,3,7,5,0,9,0,0]))
print(moving_zeroes_2(nums=[0,0,2,46,78,0,3,7,5,0,9,0,0]))