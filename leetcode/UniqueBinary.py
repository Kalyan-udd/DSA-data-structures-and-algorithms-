# CANTORS DIAGONALISATION METHOD...!

def UniqueBinary(nums):
    output = []
    
    for i in range(len(nums)):
        if nums[i][i] == "0":
            output.append("1")
        else:
            output.append("0")
        
    binary = ""
    for ch in output:
        binary = binary + ch
    return binary


print(UniqueBinary(nums=["001","111","000"]))