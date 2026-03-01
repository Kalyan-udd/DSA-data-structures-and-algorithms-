def smallest_letter_greater_than_target(letters, target):
    for ch in letters:
        if ord(ch) > ord(target):
            return ch 
    return letters[0]

def smallest_letter_greater_than_target_hasmap(letters, target):
    alpha = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26     
    }
    
    for ch in letters:
        if alpha[ch] > alpha[target]:
            return ch
    return letters[0]


print(smallest_letter_greater_than_target_hasmap(letters = ["c","f","j"], target = "a"))