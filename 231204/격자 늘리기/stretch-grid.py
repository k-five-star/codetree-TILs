n, m, k = tuple(map(int, input().split()))

arr = [input().split() for _ in range(n)]

for text in arr:
    line = ""
    
    for c in ''.join(text):
        line += c * k

    for n in range(k):
        print(line)