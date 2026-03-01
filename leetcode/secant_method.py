def f(x):
    value = x*x - 3*x - 1
    return value

def SecantMethod(x0: float,x1: float):
    if f(x0)*f(x1)>0:
        return "the values of x0 and x1 are incorrect"
    h = f(x1)-f(x0)
    x2 = round(x1-(f(x1)*(x1 - x0)/h),5)
    i = 0
    while abs(x2 - x1)>1e-7:
        if i>1000000:
            return "the function doesn't contains any roots"
        x0 = x1
        x1 = x2
        h = f(x1)-f(x0)
        x2 = round(x1-(f(x1)*(x1 - x0)/h),5)
        i += 1
    return x2

print(SecantMethod(x0=0, x1=4))