#!/usr/bin/python3

from math import cos, pi

def secant(f, p0, p1, tol=0, n0=1000):
    '''
        Newton's method requires your to fine the derivative of the function,
        which is not always easy, or possible. The secant method uses a
        succession of roots of secant lines. It uses two approximations,
        prefereably close to the solution.
       
        The Secant method will generally give problems if
        f'(x) = 0 when f(x) = 0

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
        print("n", i - 2, "pn", p0)
        if abs(p - p1) < tol:
            print("The approximate solution is", p)
            return
        i += 1
        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p1)
    
    print('The method failed after N0 iteration, N0 = ', n0)
    
if __name__ == "__main__":
    f = lambda x: cos(x) - x

    secant(f, 0.5, pi/4, tol=1*10**-8, n0=20)
