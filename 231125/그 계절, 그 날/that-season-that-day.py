def check_leap_year(year):
    if year % 4 != 0:
        return False

    if year % 100 != 0:
        return True

    if year % 400 != 0:
        return False
    
    return True

def check_valid_date(year, month, date):
    max_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and date == 29:
        return check_leap_year(year)

    if date <= max_date[month - 1]:
        return True

    return False

def tell_season(month):
    season = ["Spring", "Summer", "Fall", "Winter"]
    return season[month // 3 - 1]
         

def main():
    Y, M, D = tuple(map(int, input().split()))

    if not check_valid_date(Y, M, D):
        print(-1)
    
    else:
        print(tell_season(M))

main()