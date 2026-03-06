def CheckOnesSegment(s):
    n = len(s)
    indices = []
    for i in range(n):
        if s[i] == "1":
            if len(indices) != 0:
                if indices[-1] != i-1:
                    return False
            indices.append(i)
    return True

print(CheckOnesSegment("0000011111"))
