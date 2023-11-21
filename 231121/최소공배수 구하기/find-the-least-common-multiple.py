big, small = tuple(map(int, input().split()))
big, small = (small, big) if big < small else (big, small)
temp = 0
ans = big * small

while big % small != 0:
    temp = big % small
    
    if temp > small:
        big = temp

    else:
        big = small
        small = temp

print(ans//small)