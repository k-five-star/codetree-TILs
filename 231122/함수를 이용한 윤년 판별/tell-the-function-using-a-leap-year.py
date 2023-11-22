def tell_leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            
            return False

        return True

    return True


print("true" if tell_leap_year(int(input())) else "false")