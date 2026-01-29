def contain_duplicate(nums):
    dict = {}
    for i in nums:
        dict[i] = dict.get(i,0)+1
    for i in dict:
        if dict[i] > 1:
            return True
def contain_duplicate_1(nums):
    n = len(nums)
    set_nums = set(nums)
    m = len(set_nums)
    return n!=m
print(contain_duplicate_1( nums = [1,2,3,1]))