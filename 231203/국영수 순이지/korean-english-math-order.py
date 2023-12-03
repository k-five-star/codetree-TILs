class Student:
    def __init__(self, name, kor, eng, math):
        self.name = str(name)
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

    def print_student(self):
        print(f"{self.name} {self.kor} {self.eng} {self.math}")

student_list = [Student(*input().split()) for _ in range(int(input()))]
student_list.sort(key = lambda x : (x.kor, x.eng, x.math), reverse = True)

for student in student_list:
    student.print_student()