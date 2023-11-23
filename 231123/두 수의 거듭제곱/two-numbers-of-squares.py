def f(a, b):
    return a**b

a, b = tuple(map(int, input().split()))

print(f(a, b))