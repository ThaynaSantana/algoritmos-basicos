
def max_subarray_sum(arr):
    n, m  = len(arr), len(arr[0])

    M = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        M[i][0] = arr[i][0]
    for j in range(m):
        M[0][j] = arr[0][j]

    for i in range(1, n):
        for j in range(1, m):
            sum = arr[i][j] + M[i-1][j] + M[i][j-1] - M[i-1][j-1]

            M[i][j] = max(sum, M[i][j])

    return max(M[-1])

# Exemplo
arr = [
    [1,1,1,1],
    [2,5,-2,-9],
    [9,-5,-2,3],
    [-2,5,2,9]
]

max_sum = max_subarray_sum(arr)
print(f"Soma da submatriz de soma máxima: {max_sum}")