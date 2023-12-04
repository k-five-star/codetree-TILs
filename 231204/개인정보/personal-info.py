class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

    def print_person(self):
        print(f"{self.name} {self.height} {self.weight}")

n = 5
person_list = [Person(*input().split()) for _ in range(n)]

print("name")
person_list.sort(key = lambda x : x.name)

for person in person_list:
    person.print_person()

print()

print("height")
person_list.sort(key = lambda x : -x.height)

for person in person_list:
    person.print_person()