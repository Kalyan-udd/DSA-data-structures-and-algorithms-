def count_mono_bit(n):
    binaries = []
    for i in range(n+1):
        if i == 0:
            binaries.append("0")
        else:
            binary = ""
            while i>0:
                binary += str(i%2)
                i = i//2
            binaries.append(binary[::-1])
    count = 0
    for bina in binaries:
        value = bina[0]
        for i in bina:
            if i != value:
                break
        
            
    return count

print(count_mono_bit(4))