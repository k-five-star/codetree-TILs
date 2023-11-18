def print_nm_stars(n, m):
    print(("1" * m + "\n") * n)

row_num, col_num = tuple(map(int, input().split()))

print_nm_stars(row_num, col_num)