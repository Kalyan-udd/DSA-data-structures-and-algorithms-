import time


# Useful when you have less length of the list...!!
def TwoSumCheckBrute(nums: list[int],target: int):
    brute_i = time.perf_counter()
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return True,time.perf_counter()-brute_i
    return False, time.perf_counter() - brute_i
    
            
            
# Useful for large length of list input...!!
def TwoSumCheckBetter(nums: list[int], target: int):
    optimal_i = time.perf_counter()
    dict = {}
    n = len(nums)
    for i in range(n):
        dict[nums[i]] = dict.get(nums[i],i)
        key = target - nums[i]
        if key in dict:
            return True,time.perf_counter() - optimal_i
    return False, time.perf_counter() - optimal_i

# Useful and optimal for first kind of the problem...!
def TwoSumCheckOptimal(nums: list[int], target: int):
    start = time.perf_counter()
    n = len(nums)
    nums = sorted(nums)
    i = 0
    j = n-1
    while i<j:
        sum_ = nums[i]+nums[j]
        if sum_ == target:
            return True, time.perf_counter() - start
        elif sum_ < target:
            i += 1
        else:
            j -= 1
    return False, time.perf_counter() - start

def TwoSumCheckBrute_2(nums: list[int],target: int):
    brute_i = time.perf_counter()
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return (i,j),time.perf_counter()-brute_i
    return False, time.perf_counter() - brute_i
    

def TwoSumCheckBetter_2(nums: list[int], target: int):
    optimal_i = time.perf_counter()
    dict = {}
    n = len(nums)
    for i in range(n):
        dict[nums[i]] = dict.get(nums[i],i)
        key = target - nums[i]
        if key in dict:
            return (dict[key],i),time.perf_counter() - optimal_i
    return False, time.perf_counter() - optimal_i

def TwoSumCheckOptimal_2(nums: list[int], target: int):
    start = time.perf_counter()
    hash_map = {}
    n = len(nums)
    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i],i)
    nums = sorted(nums)
    left = 0
    right = n-1
    while left<right:
        sum_ = nums[left]+nums[right]
        if sum_ == target:
            return (hash_map[nums[right]],hash_map[nums[left]]), time.perf_counter() - start
        elif sum_ < target:
            left += 1
        else:
            right -= 1
    return False, time.perf_counter() - start

nums_1, target_1 = [1,5,8,3,4,5,9,2,4,31,65,22,34,56,34,23,45,98,23,54,67,88,555,76,777,454,444,211,232,568,334,566,7633,23445,4526,252,555,105,104,103,252,4526], 4778

print(TwoSumCheckBrute(nums=nums_1,target=target_1))
print(TwoSumCheckBetter(nums=nums_1,target=target_1))
print(TwoSumCheckOptimal(nums=nums_1, target=target_1))
print()
print(TwoSumCheckBrute_2(nums=nums_1,target=target_1))
print(TwoSumCheckBetter_2(nums=nums_1,target=target_1))
print(TwoSumCheckOptimal_2(nums=nums_1,target=target_1))