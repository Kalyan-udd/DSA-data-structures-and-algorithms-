import time

def f(x: int):
    value = (x*x) -5*x -1
    return value

def BisectionMethod(x0: int, x1: int):
    start = time.perf_counter()
    x2 = (x0 + x1)/2
    i = 0
    while abs(f(x2)) > 0.0001 and i<1000:
        if f(x2)*f(x0) < 0:
            x1 = x2
            x2 = (x0 + x1)/2
        else:
            x0 = x2
            x2 = (x0 + x1)/2
        i+=1
    return x2, time.perf_counter()-start


print(BisectionMethod(x0 = 0, x1 = 6))