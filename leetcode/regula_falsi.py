import time

def f(x: float):
    value = (x*x) - 5*x -1
    return value

def RegulaFalsiMethod(x0: float, x1:float):
    start = time.perf_counter()
    x2 = (x0*(f(x1))-x1*(f(x0)))/(f(x1)-f(x0))
    i = 0
    while abs(f(x2))>0.0001 and i < 1000:
        if f(x2)*f(x0)<0:
            x1 = x2
            x2 = (x0*(f(x1))-x1*(f(x0)))/(f(x1)-f(x0))
        else:
            x0 = x2
            x2 = (x0*(f(x1))-x1*(f(x0)))/(f(x1)-f(x0))
    return x2, time.perf_counter() - start


print(RegulaFalsiMethod(x0=0, x1=6))