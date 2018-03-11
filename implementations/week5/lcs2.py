#Uses python3

import sys


def lcs2(X, Y):
    m = len(X)
    n = len(Y)

    c = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1]+1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    return c[m][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    X = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    Y = data[:m]

    print(lcs2(X, Y))
