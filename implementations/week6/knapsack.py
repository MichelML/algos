# Uses python3
import sys

# taken from https://www.geeksforgeeks.org/knapsack-problem/
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

def optimal_weight(W, w):
    
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(knapSack(W, w, w, n))
