class paper:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 + 1000
        self.y1 = y1 + 1000
        self.x2 = x2 + 1000
        self.y2 = y2 + 1000

    def fill(self, arr):
        for i in range(self.x1, self.x2):
            for j in range(self.y1, self.y2):
                arr[i][j] = 1

    def erase(self, arr):
        for i in range(self.x1, self.x2):
            for j in range(self.y1, self.y2):
                arr[i][j] = 0

    def how_large_to_cover(self, arr):
        cx1, cy1, cx2, cy2 = self.x1, self.y1, self.x2, self.y2
        flag = 0

        for i in range(self.x1, self.x2):
            for j in range(self.y1, self.y2):
                if arr[i][j] == 1 and flag == 0:
                    cx1, cy1 = i, j
                    flag = 1

        flag = 0

        for i in range(self.x2 - 1, self.x1 - 1, -1):
            for j in range(self.y2 - 1, self.y1 - 1, -1):
                if arr[i][j] == 1 and flag == 0:
                    cx2, cy2 = i, j
                    flag = 1

        large = (cx2 - cx1 + 1) * (cy2 - cy1 + 1)
        return large


arr = [[0 for _ in range(2000)] for _ in range(2000)]
a, b, c, d = map(int, input().split())
A = paper(a, b, c, d)
A.fill(arr)

a, b, c, d = map(int, input().split())
B = paper(a, b, c, d)
B.erase(arr)

print(A.how_large_to_cover(arr))