def check(seq1, seq2):
    p1 = p2 = 0

    while p1 < len(seq1):
        if seq1[p1] == seq2[p2]:
            p1+=1
            p2+=1

        else:
            p1+=1
            p2 = 0

        if p2 == len(seq2):
            return True

    return False


tuple(map(int, input().split()))
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))

print("Yes" if check(seq1, seq2) else "No")