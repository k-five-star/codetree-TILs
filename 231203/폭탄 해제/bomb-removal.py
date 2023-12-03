class BombClear:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

info = input().split()

B1 = BombClear(*info)

print("code : " + B1.code)
print("color : " + B1.color)
print("second : " + B1.sec)