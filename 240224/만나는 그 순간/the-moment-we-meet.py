# N, M 입력받음
N, M = map(int, input().split())
# A와 B의 포지션 테이블 생성
pos_a = [0]
pos_b = [0]
# 입력과 동시에 표를 적는 함수 작성
def set_pos(arr, n):
    # n번의 입력동안
    for _ in range(n):
        # 방향과 얼마나 이동하는지를 입력받고
        d, t = input().split()
        # t회동안
        for _ in range(int(t)):
            # 다음 포지션을 방향에 따라 계산
            next_pos = arr[-1] + (1 if d == 'R' else -1)
            # 그리고 추가
            arr.append(next_pos)
# 포지션 입력받기
set_pos(pos_a, N)
set_pos(pos_b, M)
# 미팅 포인트를 -1로 초기화
ans = -1
# 시간이 지나는 동안
for i in range(1, len(pos_a)):
    # 만약 만나면
    if pos_a[i] == pos_b[i]:
        # ans를 해당 초로 설정하고
        ans = i
        # 종료
        break
# 출력
print(ans)