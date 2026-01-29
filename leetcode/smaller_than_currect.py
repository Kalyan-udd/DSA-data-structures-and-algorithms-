def smaller_than_current(nums):
    ans = []
    for i in nums:
        count = 0
        for j in nums:
            if i>j:
                count+=1
        ans.append(count)
    return ans

print(smaller_than_current(nums=[8,1,2,2,3]))