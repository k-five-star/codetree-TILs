def check(a, b):
    cnt = 0
    
    for n in range(a, b + 1):
        if any(char in str(n) for char in ["3", "6", "9"]) or n % 3 == 0:
            cnt += 1

    return cnt

a, b = tuple(map(int, input().split()))

print(check(a, b))