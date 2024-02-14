class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

    def print_student(self):
        print(self.height, self.weight, self.number)


n = int(input())
student_list = []

for i in range(1, n + 1):
    height, weight = map(int, input().split())
    student_list.append(Student(height, weight, i))

student_list.sort(key = lambda x:(x.height, x.weight))
for student in student_list:
    student.print_student()