def union_of_two_sorted_arrays(arr1, arr2):
    return list(set(arr1+arr2))

def union_of_two_sorted_array2(arr1,arr2):
    union_arr = []
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    while i < n1 and j<n2:
        if arr1[i] <= arr2[j]:
            if len(union_arr) == 0 or (union_arr[-1] != arr1[i]):
                union_arr.append(arr1[i])
            i+=1
        else:
            if len(union_arr) == 0 or (union_arr[-1] != arr2[j]):
                union_arr.append(arr2[j])
            j+=1
    while j<n2:
        if len(union_arr) == 0 or (union_arr[-1] != arr2[j]):
            union_arr.append(arr2[j])
        j+=1

    while i<n1:
        if len(union_arr) == 0 or (union_arr[-1] != arr1[i]):
            union_arr.append(arr1[i])
        i+=1
   
    return union_arr
print(union_of_two_sorted_arrays(arr1=[1,1,2,3,4,4,5], arr2 = [1,4,5,6,7,8]))
print(union_of_two_sorted_array2(arr1=[1,1,2,3,4,4,5], arr2 = [1,4,5,6,7,8]))