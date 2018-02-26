# Uses python3
# see https://proofwiki.org/wiki/Sum_of_Sequence_of_Fibonacci_Numbers
def Sum_Fib_Last_Digit(n):
    # Initialize a matrix [[1,1],[1,0]]    
    v1, v2, v3 = 1, 1, 0  
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n + 2)[3:]:
        calc = (v2*v2) % 10
        v1, v2, v3 = (v1*v1+calc) % 10, ((v1+v3)*v2) % 10, (calc+v3*v3) % 10
        if rec == '1': v1, v2, v3 = (v1+v2) % 10, v1, v2
    print((v2 - 1) % 10); 

    

if __name__ == '__main__':
    n = int(input())
    Sum_Fib_Last_Digit(n)