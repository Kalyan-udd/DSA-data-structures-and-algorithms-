def LongestBalancedSubstring2(s: str):
    frequency = {}
    n = len(s)
    max_bal = 0 
    for i in range(n):
        frequency[s[i]] = frequency.get(s[i], 0) + 1
        a = (frequency.get('a', 0))
        b = (frequency.get('b', 0))
        c = (frequency.get('c', 0))
        if (a==b==c)or((a==b)and(c==0))or((b==c)and(a==0)) or ((a==c)and(b==0)):
            max_bal = i+1
    return max_bal

print(LongestBalancedSubstring2(s = "aabcc"))
