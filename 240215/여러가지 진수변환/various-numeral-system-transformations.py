# 입력을 받는다.
N, B = map(int, input().split())
# 변환 함수
def convert(n, form):
    ans = []
    # n이 0이 될때까지 반복한다.
    while n != 0:
        # n을 form으로 나눈 나머지를 리스트의 맨 앞에 삽입
        ans.insert(0, str(n % form))
        # n을 form으로 정수형 나누기
        n //= form
    # 리스트를 반환
    return ans
# 출력한다.
print(''.join(convert(N, B)))