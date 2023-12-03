class DayInfo:
    def __init__(self, day, date, weather):
        self.day = day
        self.date = date
        self.weather = weather

    def print_day_info(self):
        print(self.day + " " + self.date + " " + self.weather)


day_list = [DayInfo(*input().split()) for _ in range(int(input()))]
rainy_list = list(filter(lambda x : x.weather == "Rain", day_list))
rainy_list.sort(key = lambda x : x.day)
rainy_list[0].print_day_info()