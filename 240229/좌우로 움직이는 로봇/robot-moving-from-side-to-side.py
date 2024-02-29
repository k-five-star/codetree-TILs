# 횟수를 입력받는다.
n, m = map(int, input().split())

# 입력받는다.
def gen_pos(cmd_arr):
    sec_pos = [0]

    for sec, cmd in cmd_arr:
        if cmd == 'R':
            sec_pos += list(range(sec_pos[-1] + 1, sec_pos[-1] + int(sec) + 1))
        else:
            sec_pos += list(range(sec_pos[-1] - 1, sec_pos[-1] - int(sec) - 1, -1))

    return sec_pos

A_pos = gen_pos([input().split() for _ in range(n)])
B_pos = gen_pos([input().split() for _ in range(m)])

ans = 0
# 1초부터 끝날때까지 실행
for i in range(1, max(len(A_pos), len(B_pos))):
    if i < len(A_pos) and i < len(B_pos):
        if A_pos[i] == B_pos[i] and A_pos[i - 1] != B_pos[i - 1]:
            ans += 1

    elif len(A_pos) <= i < len(B_pos):
        ans += B_pos[i:len(B_pos)].count(A_pos[-1])
        break

    elif len(B_pos) <= i < len(A_pos):
        ans += A_pos[i:len(A_pos)].count(B_pos[-1])
        break

print(ans)