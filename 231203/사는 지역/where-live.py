class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

    def printPerson(self):
        print("name " + self.name)
        print("addr " + self.addr)
        print("city " + self.city)

personList = [Person(*input().split()) for _ in range(int(input()))]
personList.sort(key = lambda x : x.name)
personList[-1].printPerson()