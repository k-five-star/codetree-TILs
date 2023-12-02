def div(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2

_ = input()
_list = list(map(int, input().split()))
div(_list)

for i in _list:
    print(i, end=" ")