import time
import random

def generating_list(n):
    nums = []
    for i in range(n):
        num = random.randint(0,9)
        nums.append(num)
    return nums
    

def finding_disappeared(nums):
    start_time = time.time()
    ans = []
    n = len(nums)
    freq = {}
    for i in nums:
        freq[i] = freq.get(i,0)+1
    for i in range(1,n+1):
        if i not in freq:
            ans.append(i)
    end_time = time.time()
    print(ans)
    print()
    print(len(nums))
    return(end_time - start_time)


