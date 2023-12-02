def swap(a, b):
    a, b = b, a
    print(a, b)
    

a, b = tuple(map(int, input().split()))

swap(a, b)