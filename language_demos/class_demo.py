

class Person:

    def __init__(self, first_name, last_name):
        # double underscore marks an attribute as private
        self.__first_name = first_name

        # single underscore indicates protected
        self._last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    def full_name(self):
        return self.__first_name + " " + self._last_name


# def record_info(self):
#     return self.__last_name + ", " + self.__first_name


person = Person("Bob", "Smith")

# Person.record_info = record_info
# del Person.full_name

print(person)
print(person.full_name())
# print(person.record_info())
print(person.first_name)

person.first_name = "Timmy"

# # print(person.age)

# person.age = 23
# print(person.age)

# del person.first_name

print(person.__dict__)

# print(Person)
