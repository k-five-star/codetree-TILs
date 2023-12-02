n, m = tuple(map(int, input().split()))
_list = list(map(int, input().split()))

def f(m):
    global _list
    result = []

    for _ in range(m):
        a, b = tuple(map(int, input().split()))
        result.append(sum(_list[a - 1:b]))

    for i in result:
        print(i, end = "\n")

f(m)