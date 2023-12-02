def rec(n):
    if n <= 2:
        return n

    return n + rec(n - 2)

N = int(input())
print(rec(N))