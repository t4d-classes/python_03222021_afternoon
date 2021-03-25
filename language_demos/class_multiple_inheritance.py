class Grandparent:
    def __init__(self):
        print("Grandparent")
        super().__init__()

    def do_it(self):
        print("do it: grandparent")


class ParentA(Grandparent):
    def __init__(self):
        print("ParentA")
        super().__init__()

    def do_it(self):
        print("do it: parenta")


class ParentB(Grandparent):
    def __init__(self):
        print("ParentB")
        super().__init__()

    def do_it(self):
        print("do it: parentb")


class Child(ParentB, ParentA):
    def __init__(self):
        print("Child1")
        super().__init__()

    # def do_it(self):
    #     print("do it: child")


print(Child.__mro__)

child = Child()
child.do_it()


# def do_it(self):
#     print("do it: parenta")
# ParentA.do_it = do_it


# class Child2(ParentB, ParentA):
#     def __init__(self):
#         print("Child2")
#         super().__init__()

# print(Child2.__mro__)

# child2 = Child2()
