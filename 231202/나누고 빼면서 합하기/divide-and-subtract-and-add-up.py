total = 0

def f(A, m):
    global total

    while m != 1:
        total += A[m - 1]

        if(m % 2 == 1):
            m -= 1

        else:
            m = m // 2

    total += A[m - 1]
    
_, n = tuple(map(int, input().split()))
_list = list(map(int, input().split()))

f(_list, n)

print(total)