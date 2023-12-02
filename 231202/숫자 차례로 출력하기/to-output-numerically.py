def rec_asc(n):
    if n == 0:
        return

    rec_asc(n - 1)
    print(n, end = ' ')

def rec_desc(n):
    if n == 0:
        return 

    print(n, end = ' ')
    rec_desc(n - 1)


N = int(input())

rec_asc(N)
print("")
rec_desc(N)