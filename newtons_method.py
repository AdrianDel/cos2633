#!/usr/bin/python3

from math import cos, pi, sin

def newtons_method(f, dx_f, p0, tol=0, n0=1000):
    '''
        Newton's method (also known as the Newton–Raphson method), named after
        Isaac Newton and Joseph Raphson, is a method for finding successively
        better approximations to the roots (or zeroes) of a real-valued function.
        
        Newton's method will generally give a problems if
        f'(x) = 0 when f(x) = 0
        
        f - The formula for which to find roots
        dx_f - The derivative of the formula to find root for
        p0 - An initial approximation of the root
        tol - Acceptable error tolerence for the answer
        n0, - Maximum number of iterations before giving up
    '''
    i = 1
    while i < n0:
        p = p0 - f(p0)/dx_f(p0)
        print('n', i - 1, 'pn', p0)
        if abs(p - p0) < tol:
            print(p)
            return
        i += 1
        p0 = p
    
    print('The method failed after N0 iteration, N0 = ', n0)
    
if __name__ == "__main__":
    f = lambda x: cos(x) - x
    dx_f = lambda x: -sin(x) - 1

    newtons_method(f, dx_f, pi/4, tol=1*10**-8, n0=200)
