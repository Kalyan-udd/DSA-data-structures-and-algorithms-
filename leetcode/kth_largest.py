def kth_largest(nums,k):
    n = len(nums)
    if n<2:
        return nums[0]
    nums = merge_sort(nums,0,n)
    return nums[-k]

def merge_sort(nums,low,high):
    if low==high:
        return
    mid = high-low/2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid+1,high)
    temp = merge(nums, low,mid,high)
    left = low
    while left<=high:
        nums[left] = temp[left]
    return nums
    
def merge(nums,low,mid,high):
    temp = []
    i = low
    j = mid+1
    while i<=mid and j<=high:
        if nums[i]<=nums[j]:
            temp.append(nums[i])
            i+=1
        else:
            temp.append(nums[j])
            j+=1
    while i<=mid:
        temp.append(nums[i])
        i+=1
    while j<=high:
        temp.append(nums[j])
        j+=1
    return temp


print(kth_largest(nums = [7,6,5,4,3,2,1], k= 2))
