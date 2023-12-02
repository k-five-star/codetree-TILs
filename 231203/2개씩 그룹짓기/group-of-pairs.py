_ = input()
_list = list(map(int, input().split()))

_max = -999999999999

asc = sorted(_list)
desc = reversed(asc)

for i, j in zip(asc, desc):
    if i + j > _max:
        _max = i + j

print(_max)