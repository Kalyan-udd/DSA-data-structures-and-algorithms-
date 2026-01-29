def missing_number(nums):
    n = len(nums)
    dict = {}
    for num in nums:
        dict[num] = dict.get(num,0) +1
    for i in range(n+1):
        if i not in dict:
            return i
    
print(missing_number(nums=[3,0,1]))