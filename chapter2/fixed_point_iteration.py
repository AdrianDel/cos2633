#!/usr/bin/python3

def fixed_point_iteration(g, p0, tol=0, n0=1000):
    i = 1
    while i < n0:
        p = g(p0)
        if abs(p - p0) < tol:
            print(p)
            return
        i += 1
        p0 = p
    
    print('The method failed after N0 iteration, N0 = ', n0)
    
if __name__ == "__main__":
    g = lambda x: x - (x**3 + 4*(x**2) - 10) / (3*(x**2) + 8*x)

    fixed_point_iteration(g, 1.5, tol=1*10**-8, n0=20)
