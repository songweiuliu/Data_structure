#coding: utf-8
# Fibonacci


#recursion
def fib(n):
    if n <2:
        return 1
    else:
        return fib(n-1)+fib(n-2)



#normally
def fibn(n):
    if n <2:
        f1,f2=1,1
    else:
        for i in range(1,n):
            f1,f2=f2,f2+f1
    return f2

#o(logn)
