# Check whether you can make the string equal with the other string with operation 1 or not.
def canBeEqual(s1:str,s2:str):
    even1,even2,odd1,odd2 = '','','',''
    if s1[0] < s1[2]:
        even1 = even1 + s1[0]
        even1 = even1 + s1[2]
    else:
        even1 = even1 + s1[2]
        even1 = even1 + s1[0]
    if s2[0] < s2[2]:
        even2 = even2 + s2[0]
        even2 = even2 + s2[2]~
    else:
        even2 = even2 + s2[2]
        even2 = even2 + s2[0]
    if s1[1] < s1[3]:
        odd1 = odd1 + s1[1]
        odd1 = odd1 + s1[3]
    else:
        odd1 = odd1 + s1[3]
        odd1 = odd1 + s1[1]
    if s2[1] < s2[3]:
        odd2 = odd2 + s2[1]
        odd2 = odd2 + s2[3]
    else:
        odd2 = odd2 + s2[3]
        odd2 = odd2 + s2[1]
    return even1 == even2 and odd1 == odd2
    
print(canBeEqual(s1 = "abcd", s2 = "cdab"))

