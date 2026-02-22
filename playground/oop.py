class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_people()
        print(Person.display_number_of_people())

    @classmethod
    def display_number_of_people(cls):
        print(cls.number_of_people)

    @classmethod
    def add_people(cls):
        cls.number_of_people += 1

    def introduce(self):
        print(f"Hi, my name is {self.name}")


p1 = Person("Tim")
p2 = Person("Anna")
print(type(Person))
print(type(p1))
p1.introduce()
Person.introduce(p1)
Person.display_number_of_people()
Person.display_number_of_people(Person)
