# 전염력 + 전염여부 => 0으로 배열 설정해두고, 감염시, 최초로 1+K로 업데이트, K감염 이후엔 1만 남음
# 그래서 양수면 감염된 걸로 판단. 0이면 미감염 

# 입력을 받는다.
N, K, P, T = map(int, input().split())
infected = [0 for _ in range(N + 1)]
infected[P] = 1 + K # 감염

handshake = [tuple(map(int, input().split())) for _ in range(T)]
handshake.sort(key = lambda x : x[0])

# 악수 기록을 순회하며 보기
for _, a_idx, b_idx in handshake:
    # 만약 둘 다 전파 불가능이라면 => 넘어간다.
    if infected[a_idx] <= 1 and infected[b_idx] <= 1:
        continue
    # 만약 감염(전파가능, 전파 불가능) 감염(전파 가능, 전파 불가능)이라면
    if infected[a_idx] and infected[b_idx]:
        # 1씩 감소시키되, 1이면 걍 놔둔다.
        infected[a_idx] = infected[a_idx] - 1 if infected[a_idx] > 1 else 1
        infected[b_idx] = infected[b_idx] - 1 if infected[b_idx] > 1 else 1
    # 만약 미감염과 전파 가능이라면
    else:
        # 미감염자는 1+K로 업데이트 그게 아니라 전파자면 -1
        infected[a_idx] = 1 + K if infected[a_idx] == 0 else infected[a_idx] - 1
        infected[b_idx] = 1 + K if infected[b_idx] == 0 else infected[b_idx] - 1
# 배열 순회하며 0이면 0출력, 양수면 1출력
for developer in infected[1:]:
    if developer > 0 : 
        print(1, end = '')
    else :
        print(0, end = '')