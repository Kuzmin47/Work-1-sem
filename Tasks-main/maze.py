def count_paths(n, m, i=0, j=0, memo=None):
    if memo is None:
        memo = {}
    if i == n - 1 and j == m - 1:
        return 1
    if (i, j) in memo:
        return memo[(i, j)]
    count = 0
    if i < n - 1:
        count += count_paths(n, m, i + 1, j, memo)
    if j < m - 1:
        count += count_paths(n, m, i, j + 1, memo)
    memo[(i, j)] = count
    return count
n = 3
m = 3
print("Количество возможных путей:", count_paths(n, m))
