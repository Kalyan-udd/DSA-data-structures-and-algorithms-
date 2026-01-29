def stack(target, n):
    length = len(target)
    stack = []
    output = []
    i = 1
    j = 0
    while i<=n and j<length:
        if i == target[j]:
            stack.append(i)
            output.append("push")
            i+=1
            j+=1
        else:
            output.append("push")
            output.append("pop")
            i+=1
        if stack == target:
            return output
    return output, stack

print(stack(target = [1,2], n = 4))