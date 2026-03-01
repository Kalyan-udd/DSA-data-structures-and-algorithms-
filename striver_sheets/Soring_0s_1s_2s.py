import time


def Sorting0s1sand2sBrute(nums: list[int]):
    start = time.perf_counter()
    nums = sorted(nums)
    return nums, time.perf_counter() - start


def Sorting0s1sand2sBetter(nums: list[int]):
    start = time.perf_counter()
    count_zero = 0
    count_one = 0
    count_two = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            count_zero += 1
        elif nums[i] == 1:
            count_one += 1
        else:
            count_two += 1
    print(count_zero, count_one, count_two)
    i = 0
    while i < count_zero:
        nums[i] = 0
        i += 1
    print(i)
    while i < count_zero+count_one:
        nums[i] = 1
        i+= 1
    print(i)
    while i < count_zero+count_one+count_two:
        nums[i] = 2
        i+=1
    return nums, time.perf_counter() - start


def Sorting0s1sand2sOptimal(nums: list[int]):
    start = time.perf_counter()



print(Sorting0s1sand2sBetter(nums=[0,2,1,1,0,2,0,1]))