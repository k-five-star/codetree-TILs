text = "HelloWorld"

def rec(n):
    if n == 0:
        return

    print(text)
    rec(n - 1)

rec(int(input()))