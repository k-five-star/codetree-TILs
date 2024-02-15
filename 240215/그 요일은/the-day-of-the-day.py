class Date:
    def __init__(self, month, date):
        self.month = month
        self.date = date

    @staticmethod
    def calculate_day_since_new_year(month, date):
        day_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        elapsed_day = sum(day_in_month[:month]) + date - 1
        return elapsed_day

    @staticmethod
    def calculate_day_diff(date1, date2):
        diff = Date.calculate_day_since_new_year(date2.month, date2.date) - Date.calculate_day_since_new_year(date1.month, date1.date)
        return diff

    @staticmethod
    def calculate_how_many_times_the_day_passed(diff, day):
        day_dict = {
            "Mon": 0,
            "Tue": 1,
            "Wed": 2,
            "Thu": 3,
            "Fri": 4,
            "Sat": 5,
            "Sun": 6,
        }

        times = diff // 7 + (1 if (diff % 7) >= day_dict[day] else 0)
        return times

# 사용 예시
m1, d1, m2, d2 = map(int, input().split())
day = input()

start_date = Date(m1, d1)
end_date = Date(m2, d2)

result = Date.calculate_how_many_times_the_day_passed(Date.calculate_day_diff(start_date, end_date), day)
print(result)