N, M = map(int, input().split())
pos_a = [0]
pos_b = [0]

def set_pos(arr, n):
    for _ in range(n):
        d, t = input().split()

        for _ in range(int(t)):
            next_pos = arr[-1] + (1 if d == 'R' else -1)
            arr.append(next_pos)

set_pos(pos_a, N)
set_pos(pos_b, M)

ans = -1

for i in range(1, len(pos_a)):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)