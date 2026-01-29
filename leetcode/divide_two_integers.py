def divide_two_integers(dividend,divisor):
    quotient = 0
    if dividend*divisor>=0:
        if dividend>0:
            while dividend>=1:
                dividend = dividend - divisor
                quotient+=1
            return quotient-1
        elif dividend == 0:
            return 0
        elif divisor == 0 and dividend>0:
            return 2**31-1
        elif divisor ==0 and dividend<0:
            return -2**31
        else:
            while dividend<=-1:
                dividend = dividend - divisor
                quotient += 1
            return quotient-1
    else:
        if dividend>0:
            while dividend>=1:
                dividend = dividend + divisor
                quotient+=1
            return -1*(quotient-1)
        if dividend<0:
            while dividend<=-1:
                dividend = dividend + divisor
                quotient += 1
            return -1*(quotient-1)

print(divide_two_integers(7,0))