class paper:
    def __init__(self, x, y):
        self.x = x + 100
        self.y = y + 100

    def add(self, arr):
        for i in range(self.x, self.x + 8):
            for j in range(self.y, self.y + 8):
                arr[i][j] = 1

def count(arr):
    cnt = 0

    for i in range(200):
        for j in range(200):
            if arr[i][j] == 1:
                cnt+=1

    return cnt
    
arr = [[0 for _ in range(200)] for _ in range(200)]

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    new_paper = paper(a, b)
    new_paper.add(arr)

print(count(arr))