# 무한한 타일은 어떻게 구현할 것인가? => 100 * 1000 * 2 + 1 사이즈의 리스트
# 회색, 검정, 흰색을 어떻게 표현할 것인가? => 'G', 'B', 'W'

# 사이즈
SIZE = 100 * 1000

# n을 입력받는다.
n = int(input())
# 변수를 설정한다. => 리스트, 현재 위치, 
field = ['G'] * (SIZE * 2 + 1)
cur = 0 # 이거 안되면 수정
# n번 반복한다.
for _ in range(n):
    # 명령어를 입력받는다.
    x, cmd = input().split()
    x = int(x)
    # 만약 R 이라면
    if cmd == 'R':
        # [현재 위치, 현재 위치 + x) 를 순회하면서
        for idx in range(cur, cur + x):
            # 검은색으로 바꾼다.
            field[idx] = 'B'
            # 현재 위치를 +1.
            cur = idx
    # 만약 L 이라면
    if cmd == 'L':
        # [현재 위치, 현재 위치 - x, -1)을 순회하면서
        for idx in range(cur, cur - x, -1):
            # 흰색으로 바꾼다.
            field[idx] = 'W'
            # 현재 위치를 -1.
            cur = idx
# 츨력 with count
print(field.count('W'), field.count('B'))