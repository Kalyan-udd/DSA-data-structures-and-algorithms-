def ComplementDecimal(n: int):
    output = 0
    i = 0
    if n == 0:
        return 1
    while n>0:
        if n%2 == 0:
            output += 2**i
        n = n//2
        i += 1
    return output
print(ComplementDecimal(6))