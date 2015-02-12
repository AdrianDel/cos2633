#!/usr/bin/python3

from math import cos, pi

def regula_falsi(f, p0, p1, tol=0, n0=1000):
    '''
        Also know as the method of False Position, this method generates
        approximations in the same manner as the Secant method, but includes
        a test to ensute the root is always bracketed, similar to the Bisection
        method.
        f - The formula for which to find roots
        p0 - The first initial approximation of the root
        p1 - The second initial approximation of the root
        tol - Acceptable error tolerence for the answer
        n0, - Maximum number of iterations before giving up
    '''
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= n0:
        p = p1 - (q1*(p1 - p0))/(q1 - q0)
        print("n", i - 2, "pn", p)
        if abs(p - p1) < tol:
            print("The approximate solution is", p)
            return
        i += 1
        q = f(p)

        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    
    print('The method failed after N0 iteration, N0 = ', n0)
    
if __name__ == "__main__":
    f = lambda x: x * (2.71828)**x - 2

    regula_falsi(f, 0.5, 1, tol=1*10**-8, n0=20)
