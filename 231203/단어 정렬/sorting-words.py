n = int(input())
_list = []


for _ in range(n):
    text = input()
    _list.append(text)

_list.sort()

print('\n'.join(_list))