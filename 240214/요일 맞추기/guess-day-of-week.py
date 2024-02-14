dayOfWeek = {
    0:"Mon",
    1:"Tue",
    2:"Wed",
    3:"Thu",
    4:"Fri",
    5:"Sat",
    6:"Sun"
}

lastDayOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())
delta = 0

delta += (d2 - d1)
if m1 < m2:
    delta += sum(lastDayOfMonth[m1:m2])
elif m1 > m2:
    delta -= sum(lastDayOfMonth[m2:m1])

day = dayOfWeek.get(delta % 7)
print(day)