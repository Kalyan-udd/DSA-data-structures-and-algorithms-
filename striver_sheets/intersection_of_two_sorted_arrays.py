# Brute code answer
def intersection_of_sorted_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    ans = []
    vis = []
    for i in range(n2):
        vis.append(0)
    for i in range(n1):
        for j in range(n2):
            if arr1[i] == arr2[j] and vis[j] == 0:
                ans.append(arr1[i])
                vis[j] = 1
                break
            if arr2[j] > arr1[i]:
                break

    return ans

# optimal code
def intersection_of_sorted_arrays2(arr1, arr2):
    n = len(arr1) 
    m = len(arr2)
    ans_array = []
    i = 0
    j = 0
    while i < n and j<m:
        if arr1[i] == arr2[j]:
            ans_array.append(arr1[i])
            i+=1 
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1
    return ans_array


print(intersection_of_sorted_arrays(arr1= [1,1,2,3,4,5,6,6,6,6], arr2=[1,2,2,3,4,4,4,5,6,6]))
print(intersection_of_sorted_arrays2(arr1= [1,1,2,3,4,5,6,6,6,6], arr2=[1,2,2,3,4,4,4,5,6,6]))