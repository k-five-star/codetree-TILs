_ = input()
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

print("Yes" if list_A.sort() == list_B.sort() else "No")