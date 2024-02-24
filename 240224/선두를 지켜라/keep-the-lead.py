N, M = map(int, input().split())

pos_A = [0]
pos_B = [0]
pos_diff = []
ans = 0

def set_pos(arr, n):
    for _ in range(n):
        v, t = map(int, input().split())
        sec_to_fill = len(arr)

        for i in range(sec_to_fill, sec_to_fill + t): # sec_to_fill ~ sec_to_fill + t - 1
            arr.append(arr[i - 1] + v)

set_pos(pos_A, N)
set_pos(pos_B, M)


for i in range(len(pos_A)):
    if pos_A[i] - pos_B[i] != 0:
        pos_diff.append(pos_A[i] - pos_B[i])

for i in range(1, len(pos_diff)):
    if pos_diff[i] * pos_diff[i - 1] < 0:
        ans += 1

print(ans)