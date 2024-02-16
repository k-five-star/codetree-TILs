# 사각형 클래스를 만든다.
class square:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 + 1000
        self.y1 = y1 + 1000
        self.x2 = x2 + 1000 - 1
        self.y2 = y2 + 1000 - 1

    def fill(self, arr):
        for i in range(self.x1, self.x2 + 1):
            for j in range(self.y1, self.y2 + 1):
                arr[i][j] = 1

        return arr

    def erase(self, arr):
        for i in range(self.x1, self.x2 + 1):
            for j in range(self.y1, self.y2 + 1):
                arr[i][j] = 0

        return arr

# A와 B의 입력을 받는다.
x1, y1, x2, y2 = map(int, input().split())
A = square(x1, y1, x2, y2)
x1, y1, x2, y2 = map(int, input().split())
B = square(x1, y1, x2, y2)
# 큰 배열 안에 채운다.
arr = [[0 for _ in range(2500)] for _ in range(2500)]
arr = A.fill(arr)
arr = B.fill(arr)
# M을 입력받는다.
x1, y1, x2, y2 = map(int, input().split())
M = square(x1, y1, x2, y2)
# 큰 배열에서 그만큼 지운다.
arr = M.erase(arr)
# 큰 배열에서 칠해진 부분만 계산한다.
cnt = 0

for i in range(0, 2500):
    for j in range(0, 2500):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)