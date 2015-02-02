#!/usr/bin/python3

from numpy import sqrt

def muller(f, p0, p1, p2, tol=0, n0=1000):
    '''
        Muller's method is a root finding algorithm based on the secant method.
        The secant method constructs a line through 2 points where mullter
        method uses 3 points to construct a parabola. The intersection of the
        porabola with the x-axis is the next approximation of the root

        f - The formula for which to find roots
        p0 - The first initial approximation of the root
        p1 - The second initial approximation of the root
        p2 - The third initial approximation of the root
        tol - Acceptable error tolerence for the answer
        n0, - Maximum number of iterations before giving up
    '''
    h1 = p1 - p0;
    h2 = p2 - p1;
    d1 = (f(p1) - f(p0)) / h1
    d2 = (f(p2) - f(p1)) / h2
    d = (d2 - d1) / (h2 + h1)
    
    i = 2
    while i <= n0:
        b = d2 + h2*d
        D = sqrt(b**2 - 4*f(p2) * d + 0j)

        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        h = -2*f(p2)/E
        p = p2 + h

        print(p)

        if abs(h) < tol:
            print(p)
            return

        p0 = p1
        p1 = p2
        p2 = p
        h1 = p1 - p0;
        h2 = p2 - p1;
        d1 = (f(p1) - f(p0)) / h1
        d2 = (f(p2) - f(p1)) / h2
        d = (d2 - d1) / (h2 + h1)

        i += 1

    
    print('The method failed after N0 iteration, N0 = ', n0)
    
if __name__ == "__main__":
    f = lambda x: x**4 - 3*x**3 + x**2 + x + 1

    muller(f, 0.5, -0.5, 0, tol=1*10**-8, n0=20)
