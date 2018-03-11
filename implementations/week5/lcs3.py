# #Uses python3

# NOT WORKING, DO REVISE WHEN COMING ACROSS THIS

# import sys


# def lcs2(X, Y):
#     m = len(X)
#     n = len(Y)

#     lcs_table = [[None]*(n+1) for i in range(m+1)]
#     lcs = []

#     for i in range(m+1):
#         for j in range(n+1):
#             if i == 0 or j == 0:
#                 lcs_table[i][j] = 0
#             elif X[i-1] == Y[j-1]:
#                 lcs = lcs + [X[i-1]]
#                 lcs_table[i][j] = lcs_table[i-1][j-1]+1
#             else:
#                 lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])

#     return lcs


# def lcs3(X, Y, Z):
#     return lcs2(X, Y)


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     an = data[0]
#     data = data[1:]
#     a = data[:an]
#     data = data[an:]
#     bn = data[0]
#     data = data[1:]
#     b = data[:bn]
#     data = data[bn:]
#     cn = data[0]
#     data = data[1:]
#     c = data[:cn]
#     print(lcs3(a, b, c))
