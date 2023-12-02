n, k, T = input().split()
n, k = tuple(map(int, (n, k)))
_list = []

for _ in range(n):
    text = input()

    if text[:len(T)] == T:
        _list.append(text)

_list.sort()

print(_list[k - 1])