def SuccessfulPairsOfSpellsandPortions(spells: list[int], potions: list[int], success: int):
    output = []
    n = len(spells)
    m = len(potions)
    potions = sorted(potions)
    for i in range(n):
        k = success/spells[i]
        j = 0
        while j<m and potions[j]<k:
            j+=1
        output.append(m-j)
    return output

# Using bisection method here...
def SuccessfulPairsOfSpellsandPortions_2(spells: list[int], potions: list[int], success: int):
    output = []
    n = len(spells)
    m = len(potions)
    potions.sort()
    for s in spells:
        target = (success+s-1)//s
        low = 0
        high = m
        while low < high:
            mid = (low+high)//2
            if potions[mid]<target:
                low = mid+1 
            else:
                high = mid
        output.append(m-low)
    return output

print(SuccessfulPairsOfSpellsandPortions(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))

print(SuccessfulPairsOfSpellsandPortions_2(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))
