N, K, P, T = map(int, input().split())
infected = [0 for i in range(N + 1)]
infected[P] = 1 + K
handshake = [tuple(map(int, input().split())) for _ in range(T)]
handshake.sort(key = lambda x : x[0])
for _, a_idx, b_idx in handshake:
    if infected[a_idx] <= 1 and infected[b_idx] <= 1:
        continue
    infected[a_idx] = 1 + K if infected[a_idx] == 0 else infected[a_idx] - 1
    infected[b_idx] = 1 + K if infected[b_idx] == 0 else infected[b_idx] - 1
for developer in infected[1:]:
    print(1 if developer > 0 else 0, end = '')