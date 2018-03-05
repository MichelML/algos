# Uses python3
import sys
import random


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

# taken from https://stackoverflow.com/a/36972773
def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return qsort(less) + equal + qsort(greater)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    qSorted = qsort(a)
    for x in qSorted:
        print(x, end=' ')
