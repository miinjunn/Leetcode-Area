points = [[0, 3, 0, 4, 2], [5, 4, 2, 4, 1], [5, 0, 0, 5, 1], [2, 0, 1, 0, 3]]

# dp for row[0]
prev = points[0]
print(f'this is row-0:\n{prev}')
print('-'*20)

# init m x n --> init row x col
m = len(points)
n = len(prev)

# dp for row[1] to len(row) -> 1..4
for i in range(1, m):
    print(f'this is row-{i}:')
    l_max = [0] * n
    r_max = [0] * n

    l_max[0] = prev[0]
    print(f'l_max[0] => {l_max[0]}')
    # isi tiap column pada row (l-max) from left-to-right
    for j in range(1, n):
        l_max[j] = max(l_max[j-1] - 1, prev[j])
        print(f'l_max[{j}] => {l_max[j-1] - 1, prev[j]}')

    print()
    r_max[-1] = prev[-1]
    print(f'r_max[{len(r_max)-1}] => {r_max[-1]}')
    # isi tiap column pada row (r-max) from right-to-left
    for j in range(n-2, -1, -1):
        r_max[j] = max(r_max[j+1] - 1, prev[j])
        print(f'r_max[{j}] => {r_max[j+1] - 1, prev[j]}')

    print()
    print(f'DP row-{i} => ', end='')
    for j in range(n):
        prev[j] = points[i][j] + max(l_max[j], r_max[j])
        print({prev[j]}, end=' ')

    print()
    print('-'*20)

print(max(prev))
