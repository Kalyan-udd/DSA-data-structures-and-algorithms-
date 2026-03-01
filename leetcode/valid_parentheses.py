def ValidParenthesis(s):
    n = len(s)
    i = 0
    count_sq = 0
    count_curl = 0
    count_nr = 0
    while i<n:
        if s[i] == "[":
            print("sq")
            count_sq +=1
        elif s[i] == "]":
            print("sq")
            count_sq -=1
        elif s[i] == "{":
            print("curl")
            count_curl +=1
        elif s[i] == "}":
            print("curl")
            count_curl -=1
        elif s[i] == "(":
            print("nr")
            count_nr +=1
        elif s[i] == ")":
            print("nr")
            count_nr -=1
        i += 1
    if (count_curl == 0 and count_nr == 0 and count_sq):
        return True
    return False

print(ValidParenthesis("()"))