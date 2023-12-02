def f(a, b):
    if a > b:
        return a + 25, b * 2

    else:
        return a * 2, b + 25

a, b = tuple(map(int, input().split()))

print(*f(a, b))