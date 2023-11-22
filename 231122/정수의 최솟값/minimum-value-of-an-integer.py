def add(*numbers):
    return min(numbers)

a, b, c = tuple(map(int, input().split()))

print(add(a, b, c))