def rec(n):
    if n == 0:
        return

    rec(n - 1)
    print("*" * n)


N = int(input())
rec(N)