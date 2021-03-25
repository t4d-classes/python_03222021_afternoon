
class SomeOther:
    pass


class Person(SomeOther):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def do_work(self):
        pass


class Student(Person):

    def __init__(self, student_id, first_name, last_name):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def record_info(self):
        return f"{self.student_id} {self.last_name}, {self.first_name}"

    def do_work(self):
        print("learn the content")


class Instructor(Person):

    def __init__(self, student_id, first_name, last_name):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def record_info(self):
        return f"{self.student_id} {self.last_name}, {self.first_name}"

    def do_work(self):
        print("teach the content")


# student = Student(1, "Bob", "Smith")

# print(student.full_name())
# print(student.record_info())

# print(issubclass(Student, SomeOther))
# print(isinstance(student, SomeOther))
