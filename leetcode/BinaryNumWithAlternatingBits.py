def BinaryNumWithAlternatingBits(n: int):
    string = ""
    if n < 2:
        return False
    while n>0:
        d = n%2
        n = n//2
        string = str(d) + string
    i = 0
    j = 1
    k = len(string)
    while i < k-1 :
        if string[i] == string[i+1]:
            return False
        i += 1
    return True


print(BinaryNumWithAlternatingBits(n=10))