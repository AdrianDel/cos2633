#!/usr/bin/python3

import pprint

def nevilles_iterated_interpolation(X, x, y):
    '''
    Neville's algorithm is an algorithm used for polynomial interpolation that
    was derived by the mathematician Eric Harold Neville. Given n + 1 points,
    there is a unique polynomial of degree ≤ n which goes through the given
    points. Neville's algorithm evaluates this polynomial.

    X - the value used to approximate f(X)
    x - array of arguments for f(x)
    y - array of results of f(x)

    The length of x and y must be equal
    '''

    if len(x) != len(y):
        print('x and y must be of equal length')
        return

    pp = pprint.PrettyPrinter(indent=4)
    # Create the result matrix
    Q = []
    for i in range(0, len(x)):
        Q.append([])
        for j in range(0, len(y)):
            if j == 0:
                Q[i].append(y[i])
            else:
                Q[i].append(0)
    pp.pprint(Q);
    for i in range(1, len(x)):
        for j in range(1, i + 1):
            print(j)
            Q[i][j] = ((X - x[i - j]) * (Q[i][j - 1]) - (X - x[i]) * (Q[i - 1][j - 1]))/(x[i] - x[i - j])

    pp.pprint(Q);

if __name__ == '__main__':
    nevilles_iterated_interpolation(2.1, [2.0, 2.2, 2.3], [0.6931, 0.7885, 0.8329])
