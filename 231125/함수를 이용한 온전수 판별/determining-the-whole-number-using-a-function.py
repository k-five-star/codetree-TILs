a, b = tuple(map(int, input().split()))
cnt = 0

for n in range(a, b + 1):
    if n % 2 == 0:
        continue

    if n % 10 == 5:
        continue

    if n % 3 == 0 and n % 9 != 0:
        continue

    cnt+=1

print(cnt)