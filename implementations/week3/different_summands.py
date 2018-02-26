# Uses python3
import sys


def optimal_summands(n):
    if n < 3:
        return [n]

    summands = [1, 2]
    currentSum = 3
    nextSum = 3

    for i in range(3, n + 1):
        nextSum += i
        if nextSum == n:
            summands.append(i)
            break
        elif nextSum > n:
            summands[-1] += n - currentSum
            break
        else:
            currentSum += i
            summands.append(i)

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
