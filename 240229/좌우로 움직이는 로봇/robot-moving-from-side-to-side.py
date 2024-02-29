# 입력을 받는다.
MAX = 50000
n, m = map(int, input().split())

A_sec_and_loc = [0] * (MAX + 1)
B_sec_and_loc = [0] * (MAX + 1)
A_cur_sec = B_cur_sec = 0
dist = [0] * (MAX + 1)
ans = 0
# A로봇의 움직임 기록
for _ in range(n):
    sec, cmd = input().split()
    direction = 1 if cmd == 'R' else -1

    for _ in range(int(sec)):
        A_cur_sec += 1
        A_sec_and_loc[A_cur_sec] = A_sec_and_loc[A_cur_sec - 1] + direction
# B로봇의 움직임 기록
for _ in range(m):
    sec, cmd = input().split()
    direction = 1 if cmd == 'R' else -1

    for _ in range(int(sec)):
        B_cur_sec += 1
        B_sec_and_loc[B_cur_sec] = B_sec_and_loc[B_cur_sec - 1] + direction
# 나머지 시간 채워야 한다. 
if A_cur_sec > B_cur_sec:
    for i in range(B_cur_sec + 1, A_cur_sec):
        B_sec_and_loc[i] = B_sec_and_loc[B_cur_sec]
else:
    for i in range(A_cur_sec + 1, B_cur_sec):
        A_sec_and_loc[i] = A_sec_and_loc[A_cur_sec]
# 이 둘 사이의 거리 기록
for i in range(0, max(A_cur_sec, B_cur_sec)):
    dist[i] = B_sec_and_loc[i] - A_sec_and_loc[i]
# 거리가 0이 아니다가 0이 되는 순간들을 기록
for i in range(1, max(A_cur_sec, B_cur_sec) + 1):
    if dist[i] == 0 and dist[i - 1] != 0:
        ans += 1

print(ans)