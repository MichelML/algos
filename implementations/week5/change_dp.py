# Uses python3
import sys


def get_change(m):
    if m < 3:
        return m
    
    fours = m // 4
    moduloOfFour = m % 4

    if moduloOfFour == 0:
        return fours
    elif moduloOfFour == 1 or moduloOfFour == 3:
        return fours + 1
    else:
        return fours - 1 + (moduloOfFour + 4) // 3

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
