# 변수 설정 : 2001 사이즈의 배열, n, 방향, x, ans = 0, 좌표 = 0
field = [0] * 2001
ans = 0
idx = 0
# n 입력받음
n = int(input())
# n번 반복
for _ in range(n):
    # x, 뱡향 입력받음
    x, direction = input().split()
    x = int(x) if direction == 'R' else -int(x)
    # [지금 좌표~변경좌표)만큼의 배열을 1칸씩 늘린다.
    for i in range(min(idx, idx + x), max(idx, idx + x)):
        field[i] += 1
    # 좌표 다시 갱신
    idx += x
# 배열 순회하면서 찾기
for n in field:
    if n >= 2:
        ans+=1
# 출력
print(ans)