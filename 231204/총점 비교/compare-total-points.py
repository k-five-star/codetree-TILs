class Student:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = int(s1)
        self.s2 = int(s2)
        self.s3 = int(s3)

    def getSum(self):
        return self.s1 + self.s2 + self.s3

    def print_student(self):
        print(f"{self.name} {self.s1} {self.s2} {self.s3}")

n = int(input())

student_list = [Student(*input().split()) for _ in range(n)]
student_list.sort(key = lambda x : x.getSum())

for student in student_list:
    student.print_student()