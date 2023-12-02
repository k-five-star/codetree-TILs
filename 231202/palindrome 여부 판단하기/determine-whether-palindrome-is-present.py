def isPalindrome(_str):
    return _str == _str[::-1]

print("Yes" if isPalindrome(input()) else "No")