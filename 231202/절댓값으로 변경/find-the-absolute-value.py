def f(_list):
    for i in range(len(_list)):
        _list[i] = abs(_list[i])


_ = input()
_list = list(map(int, input().split()))
f(_list)
print(*_list)