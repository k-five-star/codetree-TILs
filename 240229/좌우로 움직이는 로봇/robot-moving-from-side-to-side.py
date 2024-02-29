def make_route(move):
    route = [0]
    for t, d in move:
        for i in range(int(t)):
            if d == 'L':
                next_pos = route[-1] - 1
            else:
                next_pos = route[-1] + 1
            route.append(next_pos)
    
    return route


N, M = map(int, input().split())

move_a = [tuple(input().split()) for _ in range(N)]
move_b = [tuple(input().split()) for _ in range(M)]

route_a = make_route(move_a)
route_b = make_route(move_b)

before_a, before_b, cnt = 0, 0, 0
for i in range(1, max((len(route_a), len(route_b)))):
    if i < len(route_a) and i < len(route_b):
        now_a, now_b = route_a[i], route_b[i]
    elif i >= len(route_a):
        now_a, now_b = route_a[-1], route_b[i]
    elif i >= len(route_b):
        now_a, now_b = route_a[i], route_b[-1]

    if before_a != before_b and now_a == now_b:
        cnt += 1
    before_a, before_b = now_a, now_b

print(cnt)