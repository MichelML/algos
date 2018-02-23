# Uses python3
import sys

def get_change(m):
    fives = m % 10
    return m // 10 + fives // 5 + fives % 5 

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))