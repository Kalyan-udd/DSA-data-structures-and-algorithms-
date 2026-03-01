import time

def f(x: float):
    value = x*x - 55*x - 1000
    return value

def f_(x: float):
    value = 2*x - 3
    return value

def NewtonRaphsonMethod(x0: float):
    start = time.perf_counter()
    x1 = ((x0 - f(x0)/f_(x0)))
    i = 0
    while abs(x1-x0)>1e-7:
        if i>1000000:
            return "no roots for the function given"
        x0 = x1
        x1 = ((x0 - f(x0)/f_(x0)))
        i+=1
    return x1, time.perf_counter()-start

print(NewtonRaphsonMethod(x0=25003))