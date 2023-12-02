_ = input()
_list = list(map(int, input().split()))

def rec(gcd, add, _next):
    if gcd % _next == 0:
        return gcd

    return rec(gcd + add, add, _next)

gcd = _list[0]

for i in range(len(_list) - 1):
    gcd = rec(gcd, gcd, _list[i + 1])
    

print(gcd)