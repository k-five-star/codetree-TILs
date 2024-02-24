# N과 M을 입력받는다.
N, M = map(int, input().split())
# A와 B의 이동을 입력받는다.
A = [tuple(input().split()) for _ in range(N)]
B = [tuple(input().split()) for _ in range(M)]

A = [int(cmd[1]) if cmd[0] == 'R' else int(cmd[1]) * -1 for cmd in A]
B = [int(cmd[1]) if cmd[0] == 'R' else int(cmd[1]) * -1 for cmd in B]
# A와 B의 초당 위치를 저장할 배열을 둔다.
A_table = [0]
B_table = [0]

for time in A:
    x = time
    while x != 0:
        if x > 0:
            A_table.append(A_table[-1] + 1)
            x -= 1
        else : 
            A_table.append(A_table[-1] - 1)
            x += 1

for time in B:
    x = time
    while x != 0:
        if x > 0:
            B_table.append(B_table[-1] + 1)
            x -= 1
        else : 
            B_table.append(B_table[-1] - 1)
            x += 1  
# 만나는 시간을 기록할 변수를 둔다.
meeting_time = -1
# 한 인덱스로, 두 배열을 순회한다.
for i in range(1, len(A_table)):
    # A와 B가 만나는 지점이 있다면, 
    if(A_table[i] == B_table[i]):
        # 그 시간을 기록한다.
        meeting_time = i
        # 반복문을 종료한다.
        break
# 출력한다.
print(meeting_time)