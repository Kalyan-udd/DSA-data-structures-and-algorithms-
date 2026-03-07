import random
import time

def MinimumFlipsForAlternate(s: int):
    # removing from the start and placing at the end.
    # Pick one and replace with its conjugate.
    start = time.perf_counter()
    count = []
    s1,s2 = "",""
    n = len(s)
    for i in range(n):
        if i%2 == 0:
            s1 += "1"
            s2 += "0"
        else:
            s1 += "0"
            s2 += "1"
    for j in range(n):
        temp = s[0]
        s = s[1:]
        s = temp + s[::-1]
        s = s[::-1]
        M1 = 0
        M2 = 0
        for k in range(n):
            if s1[k] != s[k]:
                M1 += 1
            if s2[k] != s[k]:
                M2 += 1
        count.append(min(M1,M2))
    return min(count), time.perf_counter()-start



def StringCreator(n):
    s = ""
    for i in range(n):
        s += str(random.randint(0,1))
    return s


def MinimumFlipsForAlternate2(s):
    start = time.perf_counter()
    n = len(s)
    s = s+s
    alt1, alt2 = "",""
    for i in range(len(s)):
        alt1 += "0" if i%2 else "1"
        alt2 += "1" if i%2 else "0"
    result = n
    diff1, diff2 = 0,0
    left = 0
    for right in range(len(s)):
        if s[right] != alt1[right]:
            diff1 += 1
        if s[right] != alt2[right]:
            diff2 += 1
        if (right - left + 1) > n:
            if s[left] != alt1[left]:
                diff1 -= 1
            if s[left] != alt2[left]:
                diff2 -= 1
            left +=1
        if (right - left + 1) == n:
            result = min(result, diff1, diff2)
    return result , time.perf_counter() - start
    


def MinimumFlipsForAlternate3(s):
    start = time.perf_counter()
    n = len(s)
    s = s+s
    alt1, alt2 = "",""
    for i in range(len(s)):
        alt1 += "0" if i%2 else "1"
        alt2 += "1" if i%2 else "0"
    diff1, diff2 = 0,0
    if n%2 ==1:
        result = n
        left = 0
        for right in range(len(s)):
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1
            if (right - left + 1) > n:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left +=1
            if (right - left + 1) == n:
                result = min(result, diff1, diff2)
        return result, time.perf_counter()-start
    else:
        for j in range(n):
            if s[j] != alt1[j]:
                diff1 += 1
            if s[j] != alt2[j]:
                diff2 += 1
        return min(diff1, diff2), time.perf_counter()-start


s = StringCreator(1000)


print(MinimumFlipsForAlternate(s))
print(MinimumFlipsForAlternate2(s))
print(MinimumFlipsForAlternate3(s))