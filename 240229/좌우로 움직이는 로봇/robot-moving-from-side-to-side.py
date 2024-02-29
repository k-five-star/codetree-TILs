# 입력을 받는다.
n, m = map(int, input().split())

A_sec_and_loc = [0]
B_sec_and_loc = [0]
A_cur_sec = B_cur_sec = 0
dist = [0]
ans = 0

# A로봇의 움직임 기록
for _ in range(n):
    sec, cmd = input().split()
    start = end = 0

    if cmd == 'R':
        start = A_sec_and_loc[-1] + 1
        end = start + int(sec)
        A_sec_and_loc += list(range(start, end))
    else:
        start = A_sec_and_loc[-1] - 1
        end = start - int(sec)
        A_sec_and_loc += list(range(start, end, -1))


# B로봇의 움직임 기록
for _ in range(m):
    sec, cmd = input().split()
    start = end = 0

    if cmd == 'R':
        start = B_sec_and_loc[-1] + 1
        end = start + int(sec)
        B_sec_and_loc += list(range(start, end))
    else:
        start = B_sec_and_loc[-1] - 1
        end = start - int(sec)
        B_sec_and_loc += list(range(start, end, -1))


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