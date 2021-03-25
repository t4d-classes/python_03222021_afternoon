person = {
    "first_name": "Bob",
    "last_name": "Smith"
}

print(person["age"])


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


person2 = Person("Bob", "Smith")

print(person2.age)
