a, b = map(int, input().split())
n = input()

temp = int(n, a)
ans = []

while temp != 0:
    ans.insert(0, str(temp % b))
    temp //= b

print(''.join(ans))