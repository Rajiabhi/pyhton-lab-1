def print_series(n):
    a, b = 1, 1
    print(a, b, end=' ')
    for _ in range(n - 2):
        a, b = b, a + b
        print(b, end=' ')

# Example usage
n = 7
print_series(n)
