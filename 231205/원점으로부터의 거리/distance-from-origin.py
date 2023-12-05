class Point:
    def __init__(self, num, x, y):
        self.num = int(num)
        self.x = int(x)
        self.y = int(y)
        self.manhattan_distance = abs(self.x) + abs(self.y)

n = int(input())

point_list = [Point(i, *input().split()) for i in range(1, n + 1)]
point_list.sort(key = lambda x : x.manhattan_distance)

for point in point_list:
    print(point.num)