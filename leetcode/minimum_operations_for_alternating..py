def MinimumOperationsAlternatingBinary(s: str):
    n = len(s)
    alt1, alt2 = "", ""
    for i in range(n):
        if i%2 == 0:
            alt1 += "1"
            alt2 += "0"
        else:
            alt2 += "1"
            alt1 += "0"
    diff1, diff2 = 0,0
    for i in range(n):
        if s[i] != alt1[i]:
            diff1 += 1
        if s[i] != alt2[i]:
            diff2 += 1
    return min(diff1, diff2)

print(MinimumOperationsAlternatingBinary("1111"))