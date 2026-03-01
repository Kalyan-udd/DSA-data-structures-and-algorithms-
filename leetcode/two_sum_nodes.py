def AddTwoNumbers(l1: list[int], l2: list[int]):
    n1 = len(l1)
    n2 = len(l2)
    output = []
    num1,num2 = 0,0
    for i in range(n1-1, -1,-1):
        num1 = num1*10
        num1 = num1 + l1[i]
    for j in range(n2-1, -1,-1):
        num2 = num2*10
        num2 = num2 + l2[j]
    total = str(num1 + num2)
    k = len(total)-1
    while k>=0:
        output.append(int(total[k]))
        k-=1
    return output



print(AddTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))