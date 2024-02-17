def find_remaining_area(x1, y1, x2, y2, x3, y3, x4, y4):
    # 겹치는 영역의 좌표를 찾습니다.
    overlap_x1 = max(x1, x3)
    overlap_y1 = max(y1, y3)
    overlap_x2 = min(x2, x4)
    overlap_y2 = min(y2, y4)
    
    # 겹치는 영역의 넓이를 계산합니다.
    overlap_area = 0
    if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
        overlap_area = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)

    # 첫 번째 직사각형의 전체 넓이에서 겹치는 영역의 넓이를 뺍니다.
    total_area = (x2 - x1) * (y2 - y1)
    
    # 겹치는 영역이 첫 번째 직사각형 내에 완전히 포함되지 않는 경우, 남는 영역을 재계산합니다.
    remaining_area = total_area - overlap_area
    if overlap_x1 == x1 and overlap_x2 == x2:
        if overlap_y1 > y1 or overlap_y2 < y2:
            remaining_area = (x2 - x1) * (y2 - y1) - overlap_area
    elif overlap_y1 == y1 and overlap_y2 == y2:
        if overlap_x1 > x1 or overlap_x2 < x2:
            remaining_area = (x2 - x1) * (y2 - y1) - overlap_area
    elif overlap_area == 0:  # 겹치는 영역이 없는 경우
        remaining_area = total_area

    return remaining_area

# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 겹치는 영역의 넓이 계산
overlap_area = find_overlap_area(x1, y1, x2, y2, x3, y3, x4, y4)

# 잔해물의 넓이 계산
remaining_area = calculate_remaining_area(x1, y1, x2, y2, overlap_area)

print(remaining_area)