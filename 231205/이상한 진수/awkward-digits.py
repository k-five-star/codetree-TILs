a = input()
b = input()

can_a = []
can_b = []

for idx, c in enumerate(list(a)):
    new_a = a[0:idx] + ("1" if a[idx] == "0" else "0") + a[idx + 1:]
    can_a.append(int(new_a, 2))

for idx, c in enumerate(list(b)):
    new_b = [b[0:idx] + c + b[idx + 1:] for c in ("0", "1", "2")]
    new_b.pop(int(c))
    can_b += [int(n, 3) for n in new_b]


n = set(can_a) & set(can_b)
print(*n)