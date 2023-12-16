N = int(input())
A = [0] + [int(input()) for _ in range(N)]

M = int(input())
B = [0] + [int(input()) for _ in range(M)]

cnt = 0
idx = []

for i in range(1, len(A) - len(B) + 2):
    sorted_partial_A = sorted(A[i:i + len(B) - 1])
    sorted_B = sorted(B[1:])
    delta = sorted_partial_A[0] - sorted_B[0]
    
    mapped_B = list(map(lambda x : x + delta, sorted_B))

    if mapped_B == sorted_partial_A:
        cnt+=1
        idx.append(i)

print(cnt)

for i in idx:
    print(i)