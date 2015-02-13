#!/usr/bin/python3

def nddf(x, y):
    '''

    '''

    F = []
    c = 0
    for i in x:
        F.append([])
        for j in y:
            F[c].append(0)
        c += 1

    c = 0
    for j in y:
        F[c][0] = j
        c += 1

    for i in range(1, len(x)):
        for j in range(1, len(y)):
            F[i][j] = ((F[i][j-1] - F[i-1][j-1]) / (x[i] - x[i-j]))

    print(F)

if __name__ == '__main__':
    nddf([1, 1.3, 1.6, 1.9, 2.2], [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])
