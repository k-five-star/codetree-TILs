class Student:
    def __init__(self, num, height, weight):
        self.num = int(num)
        self.height = int(height)
        self.weight = int(weight)


n = int(input())
student_list = [Student(i + 1, *input().split()) for i in range(n)]
student_list.sort(key = lambda x : (-x.height, -x.weight, x.num))

for studnet in student_list:
    print("{} {} {}".format(studnet.height, studnet.weight, studnet.num))