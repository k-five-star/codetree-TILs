n = int(input())
_list = list(map(int, input().split()))
result = []

for i in range(n):
    result.append(_list[i])
    result.sort()

    if i % 2 == 0:
        print(result[i // 2], end = ' ')