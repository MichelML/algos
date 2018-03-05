# Uses python3
import sys

# taken from http://python3.codes/binary-search/
def binary_search(number, array, lo, hi):
    if hi < lo:
        return -1      
    mid = (lo + hi) // 2        
    if number == array[mid]:
        return mid                  
    elif number < array[mid]:
        return binary_search(number, array, lo, mid - 1)
    else:
        return binary_search(number, array, mid + 1, hi)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(x, a, 0, len(a) - 1), end=' ')
