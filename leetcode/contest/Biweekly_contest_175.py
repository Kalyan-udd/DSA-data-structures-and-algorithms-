def ReverseByType(s):
    indices = []
    result = []
    letters = ""
    special_char = ""
    n = len(s)
    for i in range(n):
        result.append(s[i])
    for i in range(n):
        if ord(s[i]) > 96:
            letters+=s[i]
            indices.append(i)
    letters = letters[::-1]
    for i in range(len(indices)):
        result[indices[i]] = letters[i]
    indices.clear()
    for i in range(n):
        if ord(s[i]) < 96:
            special_char+=s[i]
            indices.append(i)
    special_char = special_char[::-1]
    for i in range(len(indices)):
        result[indices[i]] = special_char[i]
    result_s = ''
    for i in result:
        result_s += i
    return result_s    
