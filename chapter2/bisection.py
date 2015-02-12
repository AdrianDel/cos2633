#!/usr/bin/python3

from math import *
import sys

def bisect(f, a, b, tol=0, n=1000):
    '''
        If you have function f wich is defined on the interval [a,b], with
        f(a) and f(b) of oposite signs, then there exists a value c where
        f(c) = 0.
        Bisection, or the Binary-search method, is used to solve x in f(x) = 0
        f - The formula
        a - The start of the interval
        b - The end of the interval
        tol - Tolerance to use for the value
        n - Maximum number of iterations
    '''

    i = 1
    # compute the value of f(a)
    FA = f(a)
    while i <= n:
        #compute the midpoint between a and b
        p = a + (b - a) / 2
        FP = f(p)
        print(i, ":", a, b, p, FP)
        if FP == 0 or (b - a) / 2 < tol:
            print(FP)
            exit(0)
        i += 1
        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p

    print('Bisect failed after n iterations, n =', n)

if __name__ == '__main__':
    f = sys.argv[1]
    a = sys.argv[2]
    b = sys.argv[3]

    f = eval(f)

    bisect(f, float(a), float(b), tol=1*10**-3, n=3)
