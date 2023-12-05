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


def find_min_max(a, b):
    candi_list = []

    idx_a_max = a.find('0')
    max_a = a[:idx_a_max] + "1" + a[idx_a_max + 1:]
    candi_list.append(int(max_a, 2))

    idx_b_max = b.find('1') if b.find('1') < b.find('0') else b.find('0')
    max_b = b[:idx_b_max] + "2" + b[idx_b_max + 1:]
    candi_list.append(int(max_b, 3))

    idx_a_min = a[1:].find('1') + 1
    min_a = a[:idx_a_min] + "0" + a[idx_a_min + 1:]
    candi_list.append(int(min_a, 2))

    idx_b_min = a[1:].find('1') if a[1:].find('1') < a[1:].find('2') else a[1:].find('2')
    min_b = b[:idx_b_min + 1] + "0" + b[idx_b_min + 2:]
    candi_list.append(int(min_b, 3))

    return min(candi_list), max(candi_list)


SIZE = 1000000000 #범위 : 0~10억

a = input() #str타입
b = input() #str타입

_min, _max = find_min_max(a, b)

for n in range(_min, _max + 1):
    ta = bin(n)
    ta = "0" * (len(a) - len(ta[2:])) + ta[2:]
    tb = trit(n)
    tb = "0" * (len(b) - len(tb)) + tb

    if(diff(ta, a) == 1 and diff(tb, b) == 1):
        print(n)
        break