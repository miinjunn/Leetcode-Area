# Input:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(matrix)
result = [[matrix[j][i] for j in range(n-1, -1, -1)] for i in range(n)]

for i in range(n):
    matrix[i] = result[i]
print(matrix)
