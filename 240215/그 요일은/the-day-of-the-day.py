m1, d1, m2, d2 = map(int, input().split())
A = input()

def elapsed_days_from_new_year(month, day):
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elapsed_days = sum(days_in_month[1:month]) + day - 1

    return elapsed_days

num_of_day = {
    "Mon" : 0,
    "Tue" : 1,
    "Wed" : 2,
    "Thu" : 3,
    "Fri" : 4,
    "Sat" : 5,
    "Sun" : 6,
}

start_date = elapsed_days_from_new_year(m1, d1)
end_date = elapsed_days_from_new_year(m2, d2)
diff = end_date - start_date
ans = diff // 7 + 1 if diff % 7 <= num_of_day[A] else 0
print(ans)