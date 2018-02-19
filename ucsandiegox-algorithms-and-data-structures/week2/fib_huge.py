# Uses python3
# inspired from https://stackoverflow.com/a/14662102
# and https://stackoverflow.com/a/27205510

def multiply_2by2_matrices(m1, m2):
    res = [[0, 0], [0, 0]]
    for i in range(0, len(m1)):
        for j in range(0, len(m2[0])):
            sum = 0
            for k in range(0, len(m1[0])):
                sum += m1[i][k] * m2[k][j]
            res[i][j] = sum
    return res

def fib_huge(nth_fibonacci):
    base_case = [[1, 1], [1, 0]] 
    result = [[1, 1], [1, 0]]   
    for _ in range(1, nth_fibonacci):
        result = multiply_2by2_matrices(result, base_case)
    
    return result[0][1]


# real solution
# taken from https://stackoverflow.com/a/40117659
def Huge_Fib(n,m):
    # Initialize a matrix [[1,1],[1,0]]    
    v1, v2, v3 = 1, 1, 0  
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    print(v2);        

# real solution
# taken from https://stackoverflow.com/a/40557208
def fibmod(n, m):
    assert 1 <= n <= 10**18, n
    assert 2 <= m <= 10**5, m

    def f(n):
        if n == 0:
            return 0, 1
        else:
            a, b = f(n // 2)
            c = a * (2*b - a) % m
            d = (a**2 + b**2) % m

            if n % 2 == 0:
                return c, d
            else:
                return d, (c + d) % m

    return f(n)[0]

if __name__ == '__main__':
    n, m = map(int, input().split())
    Huge_Fib(n, m)
