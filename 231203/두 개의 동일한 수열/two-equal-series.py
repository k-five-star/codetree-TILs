_ = input()
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

list_A.sort()
list_B.sort()

print("Yes" if list_A == list_B else "No")