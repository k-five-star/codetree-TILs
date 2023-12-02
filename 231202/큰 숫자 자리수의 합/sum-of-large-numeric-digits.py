a, b, c = tuple(map(int, input().split()))
num = a * b * c

def rec(n):
    if n // 10 == 0:
        return n

    return rec(n // 10) + (n % 10)

print(rec(num))