N, M = map(int, input().split())

def gen_pos_per_sec(cmd_arr):
    pos = [0]

    for v, t in cmd_arr:
        pos += list(range(pos[-1] + v, pos[-1] + v * t + 1, v))

    return pos

A_pos = gen_pos_per_sec([tuple(map(int, input().split())) for _ in range(N)])
B_pos = gen_pos_per_sec([tuple(map(int, input().split())) for _ in range(M)])

ans = 0

for i in range(1, len(A_pos)):
    gap = lambda x : A_pos[x] - B_pos[x]

    if gap(i) != 0: # 양수거나, 음수거나. 바뀌었단건, 이전과 곱했을 때 0이거나 음수
        if gap(i) * gap(i - 1) <= 0:
            ans += 1
    
    else: # 0이란 것. 이전에 0이 아니기만 하면 됨
        if gap(i - 1) != 0:
            ans += 1

print(ans)