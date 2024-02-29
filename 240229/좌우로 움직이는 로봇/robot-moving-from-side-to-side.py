# 입력을 받는다.
MAX = 50000
n, m = map(int, input().split())

A_sec_and_loc = [0]
B_sec_and_loc = [0]
A_cur_sec = B_cur_sec = 0
dist = [0]
ans = 0

# A로봇의 움직임 기록
for _ in range(n):
    sec, cmd = input().split()
    direction = 1 if cmd == 'R' else -1

    for _ in range(int(sec)):
        A_cur_sec += 1
        A_sec_and_loc.append(A_sec_and_loc[A_cur_sec - 1] + direction)

# B로봇의 움직임 기록
for _ in range(m):
    sec, cmd = input().split()
    direction = 1 if cmd == 'R' else -1

    for _ in range(int(sec)):
        B_cur_sec += 1
        B_sec_and_loc.append(B_sec_and_loc[B_cur_sec - 1] + direction)

# pop한다.
A_past = A_sec_and_loc.pop(0)
B_past = B_sec_and_loc.pop(0)
A_now = B_now = 0
# 두 배열 중 하나가 없어질 때까지 반복
while len(A_sec_and_loc) and len(B_sec_and_loc):
    # pop
    A_now, B_now = A_sec_and_loc.pop(0), B_sec_and_loc.pop(0)
    # 둘의 거리 차이가 0인가? 이전에는 0이 아니었는가
    if A_now == B_now and A_past != B_past:
        # ans += 1을 한다.
        ans += 1        
    # 업데이트 한다.
    A_past, B_past = A_now, B_now

# A가 좀 남았다면
ans += A_sec_and_loc.count(B_now)
# B가 좀 남았다면
ans += B_sec_and_loc.count(A_now)
print(ans)