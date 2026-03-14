def MinimumIndex(capacity: list[int], itemSize: int):
    n = len(capacity)
    min_index = -1
    for i in range(n):
        if min_index == -1 and capacity[i]>=itemSize:
            min_index = i
        if capacity[i]>=itemSize and capacity[min_index]>capacity[i]:
            min_index = i
    return min_index


def SmallestBalancedIndex(nums: list[int]):
    n = len(nums)
    product = nums[n-1]
    sum_ = 0
    for i in range(n-2, -1, -1):
        sum_ += nums[i]
    for i in range(n-2, 0, -1):
        sum_ -= nums[i]
        if sum_ == product:
            return i
        product = product * nums[i]
    return -1

    

print(SmallestBalancedIndex([678,839,164,421,27,779,132,955,851,647,674,393,807,758,839,983,67,125,575,447,525,882,886,21,758,121,28,621,908,962,807,226,447,859,4,602,665,70,604,286,865,586,4,835,570,69,670,479,51,51,894,202,140,512,707,416,683,173,541,25,353,952,865,822,685,683,707,537,473,477,844,503,872,508,804,51,87,285,688,603,476,138,715,395,519,133,903,982,103,108,577,344,438,664,672,792,753,615,931,411,314,445,29,988,503,461,208,651,326,985,609,371,400,713,818,577,703,115,608,838,172,153,38,363,887,836,924,865,124,995,210,378,411]))

    