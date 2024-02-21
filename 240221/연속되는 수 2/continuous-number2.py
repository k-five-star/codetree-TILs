# 횟수를 입력받는다.
N = int(input())
temp = 0
cnt = 0
max_ = 0
# 그 횟수만큼 반복한다.
for i in range(N):
    # 숫자를 새로 입력받는다.
    number = int(input())
    # 이번이 처음이다. or 이전 숫자와 같다.
    if i == 0 or number == temp:
        # 횟수를 늘린다.
        cnt+=1
        # 이번 숫자를 이전 숫자에 저장한다.
        temp = number
        # max와 횟수를 비교한다. 횟수가 더 크면 max를 업데이트 한다.
        if max_ < cnt:
            max_ = cnt
    # 그게 아니다.
    else:
        # 횟수를 1으로 초기화한다.
        cnt = 1
        # 이번 숫자를 이전 숫자에 저장한다.
        temp = number
# max를 출력한다.
print(max_)