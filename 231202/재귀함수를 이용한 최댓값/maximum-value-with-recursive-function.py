def rec_max(l):
    if len(l) == 1:
        return l[0]

    return max(l[0], rec_max(l[1:]))

_ = input()
_list = list(map(int, input().split()))

print(rec_max(_list))