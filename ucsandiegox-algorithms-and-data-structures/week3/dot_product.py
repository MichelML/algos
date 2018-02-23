#Uses python3

import sys

def sortDescending(l):
    return sorted(l, reverse=True)

def max_dot_product(a, b):
    res = 0
    sortedA = sortDescending(a)
    sortedB = sortDescending(b)
    for i in range(len(a)):
        res += sortedA[i] * sortedB[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
