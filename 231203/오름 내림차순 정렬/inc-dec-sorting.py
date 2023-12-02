_ = input()
_list = list(map(int, input().split()))

for i in sorted(_list):
    print(i, end = ' ')

print()

for i in sorted(_list)[::-1]:
    print(i, end = ' ')