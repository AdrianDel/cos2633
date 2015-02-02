#!/usr/bin/python3

from math import cos, pi

def horner(x0, *a):
    '''
        Horner's method is an algorithm to calculate a polynomial at
        f(x0) and f'(x0)
         
        x0 - The value to avaluate
        a - An array of the coefficients

        The degree is the polynomial is set equal to the number of coefficients
    '''
    n = len(a)

    y = a[0]
    z = a[0]

    for j in range(1, n - 1):
        y = x0 * y + a[j]
        z = x0 * z + y

    y = x0 * y + a[-1]

    print('P(x0) =', y)
    print('P\'(x0) =', z)
    
if __name__ == "__main__":
    horner(-2, 2, 0, -3, 3, -4)
