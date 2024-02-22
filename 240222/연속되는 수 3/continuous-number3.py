# N입력받기
N = int(input())
# 배열 생성
arr = [int(input()) for _ in range(N)]
# 변수 ans, cnt 생셩
ans = cnt = 0
# 반복문으로 배열 순회하기
for i in range(N):
    # 만약 지금이 처음 or 이전 요소와 부호가 같다
    if i == 0 or arr[i] * arr[i - 1] > 0:
        # cnt를 증가시킴
        cnt += 1
    # 그게 아니다.
    else:
        # cnt초기화
        cnt = 1
    # cnt와 ans를 비교
    ans = max(ans, cnt)
# 출력
print(ans)