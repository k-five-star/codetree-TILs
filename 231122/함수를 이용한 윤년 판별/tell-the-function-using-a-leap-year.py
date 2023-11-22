def tell_leap_year(n):
    ans = True

    if n % 4 == 0:
        ans = True

    if n % 4 == 0 and n % 100 == 0:
        ans = False

    if n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        ans = True

    return ans


print("true" if tell_leap_year(int(input())) else "false")