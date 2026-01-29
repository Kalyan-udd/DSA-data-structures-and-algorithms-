def majority_element(nums):
    n = len(nums)
    dict = {}
    for i in nums:
        dict[i] = dict.get(i,0)+1
    for key in dict:
        if dict[key]>n//2:
            return key


print(majority_element([2,2,1,1,1,2,2]))