def vowel_consonent_score(s):
    dict = {
        "vowel" : ["a","e","i","o","u"],
        "consonents": ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    }
    v = 0
    c = 0
    for i in s:
        if i in dict["vowel"]:
            v+=1
        elif i in dict["consonents"]:
            c+=1
    if c>0:
        return v//c
    return 0 
        
print(vowel_consonent_score(s = "cooear"))