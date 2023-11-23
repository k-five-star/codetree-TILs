def tell_leap_year(n):
    if n % 4 != 0:
        return False

    if n % 100 != 0:
        return True

    if n % 400 != 0:
        return False

    return True

print("true" if tell_leap_year(int(input())) else "false")