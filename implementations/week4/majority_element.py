# Uses python3
import sys

def get_majority_element(a):
    targetToExceed = len(a) // 2
    registry = {}
    for el in a:
        if el in registry: registry[el] += 1
        else: registry[el] = 1
        
        if registry[el] > targetToExceed:
            return el
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
