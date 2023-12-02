def rec(n):
    if n // 10 == 0:
        return n ** 2

    return rec(n // 10) + (n % 10) ** 2

N = int(input())
print(rec(N))