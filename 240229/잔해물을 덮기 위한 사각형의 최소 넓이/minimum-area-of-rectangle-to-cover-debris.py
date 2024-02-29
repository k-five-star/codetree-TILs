# 사각형이란 클래스
class square:
    # 초기화 : x1 y1 x2 y2
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 + 1000
        self.y1 = y1 + 1000
        self.x2 = x2 + 1000 - 1
        self.y2 = y2 + 1000 - 1
    # 채우기 : 2차원 배열에 사각형을 채운다
    def fill(self, field):
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                field[x][y] = 1
    # 지우기 : 2차원 배열에 사각형을 지운다
    def erase(self, field):
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                field[x][y] = 0
    # 너비 출력 : 남아있는 애들을 다 채우기 위한 너비 확인
    def check_width(self, field):
        length = 0
        height = 0

        for x in range(self.x1, self.x2 + 1):
            flag = 0

            for y in range(self.y1, self.y2 + 1):
                if field[x][y] == 1:
                    flag = 1
                    break

            if flag == 1:
                length+=1

        for y in range(self.y1, self.y2 + 1):
            flag = 0

            for x in range(self.x1, self.x2 + 1):
                if field[x][y] == 1:
                    flag = 1
                    break

            if flag == 1:
                height+=1

        return height * length

x1, y1, x2, y2 = map(int, input().split())
s1 =  square(x1, y1, x2 ,y2)
x1, y1, x2, y2 = map(int, input().split())
s2 =  square(x1, y1, x2 ,y2)
field = [[0 for _ in range(2001)] for _ in range(2001)]

s1.fill(field)
s2.erase(field)
print(s1.check_width(field))