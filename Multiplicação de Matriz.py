# Matrix Mi has dimension
# p[i-1] x p[i] for i = 1..n
import time
start_time = time.time()

import random
def MatrixChainOrder(p, n):
    # For simplicity of the program, one
    # extra row and one extra column are
    # allocated in dp[][]. 0th row and
    # 0th column of dp[][] are not used
    dp = [[0 for i in range(n)]
          for i in range(n)]

    # dp[i, j] = Minimum number of scalar
    # multiplications needed to compute
    # the matrix M[i]M[i+1]...M[j] = M[i..j]
    # where dimension of M[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        dp[i][i] = 0

    # Simply following above recursive formula.
    for L in range(1, n - 1):
        for i in range(n - L):
            dp[i][i + L] = min(dp[i + 1][i + L] +
                               p[i - 1] * p[i] * p[i + L],
                               dp[i][i + L - 1] +
                               p[i - 1] * p[i + L - 1] * p[i + L])

    return dp[1][n - 1]


# Driver code
arr = [10, 20, 30, 40, 30]
size = len(arr)
print("Menor quantidade de multiplicação de escalares:",
      MatrixChainOrder(arr, size))



#tamanho = len(A)
#print("Menor quantidade de multiplicação de escalares:",MatrixChainOrder(A, tamanho))

end_time= time.time()
tempo= end_time - start_time
print("tempo de execução:", tempo)