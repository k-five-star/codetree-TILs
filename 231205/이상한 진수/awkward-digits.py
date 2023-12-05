def trit(n):
    val = ""
    while(n):
        k = n % 3
        val = str(k) + val
        n //= 3

    return val

def diff(a, b):
    cnt = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            cnt+=1
    return cnt

SIZE = 1000000000 #범위 : 0~10억

a = input() #str타입
b = input() #str타입

for n in range(0, SIZE + 1):
    ta = bin(n)
    ta = "0" * (len(a) - len(ta[2:])) + ta[2:]
    tb = trit(n)
    tb = "0" * (len(b) - len(tb)) + tb

    if(diff(ta, a) == 1 and diff(tb, b) == 1):
        print(n)
        break