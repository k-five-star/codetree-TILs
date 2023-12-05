class Person:
    def __init__(self, name, height, weight):
        self.name = str(name)
        self.height = int(height)
        self.weight = int(weight)

    def print_person(self):
        print(f"{self.name} {self.height} {self.weight}")


n = int(input())

person_list = [Person(*input().split()) for _ in range(n)]
person_list.sort(key = lambda x : (x.height, -x.weight))

for person in person_list:
    person.print_person()