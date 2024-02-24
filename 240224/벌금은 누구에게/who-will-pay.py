# 입력을 받는다. : 학생 수, 벌칙 횟수, 벌칙 임계치
num_of_student, n, limit = map(int, input().split())
# 학생 수 크기의 배열을 만든다.
student_list = [0] * (num_of_student + 1)
# 플래그 초기화
flag = 0
# 벌칙 횟수만큼의 반복문 실행
for _ in range(n):
    # 학생 번호를 입력 받는다.
    student_number = int(input())
    # 해당 학생의 벌칙 카운트를 1 올린다.
    student_list[student_number] += 1
    # 해당 학생이 벌칙 임계치에 도달했는가?
    if student_list[student_number] >= limit:
        # 학생 번호를 출력한다.
        print(student_number)
        # 플래그를 1로 설정하고
        flag = 1
        # 반복문을 나간다. 
        break
# 불린 학생이 없으면 -1 출력
if flag == 0:
    print(-1)