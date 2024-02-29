# 전염력 + 전염여부 => 0으로 배열 설정해두고, 감염시, 최초로 1+K로 업데이트, K감염 이후엔 1만 남음
# 그래서 양수면 감염된 걸로 판단. 0이면 미감염 

# 입력을 받는다.
N, K, P, T = map(int, input().split())
infected = [0 for i in range(N + 1)]
infected[P] = 1 + K

handshake = [tuple(map(int, input().split())) for _ in range(T)]
handshake.sort(key = lambda x : x[0])

# 악수 기록을 순회하며 보기
for _, a_idx, b_idx in handshake:
    # 만약 둘 다 전파 불가능이라면 => 넘어간다.
    if infected[a_idx] <= 1 and infected[b_idx] <= 1:
        continue

    infected[a_idx] = 1 + K if infected[a_idx] == 0 else max(infected[a_idx] - 1, 1)
    infected[b_idx] = 1 + K if infected[b_idx] == 0 else max(infected[b_idx] - 1, 1)
# 배열 순회하며 0이면 0출력, 양수면 1출력
for developer in infected[1:]:
    print(1 if developer > 0 else 0, end = '')