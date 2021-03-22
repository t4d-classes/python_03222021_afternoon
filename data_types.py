

some_var = None
print(type(some_var))

some_var = 2
print(type(some_var))

some_var = 3.0
print(type(some_var))

some_var = "hi everyone! who wants to get our early today?"
print(type(some_var))

some_var = False
print(type(some_var))

# tuple - immutable
some_var = (1, "fun", True)
print(type(some_var))
# print(some_var[1])
# shopping_cart_item = ("Apples", 3, 1.45)

# list - mutable
some_var = [1, 2, 3, 4, 5]
print(type(some_var))
# some_var.append(10)
# some_var.remove(3)
# print(some_var)


def do_it():
    print("did it")


print(type(do_it))
some_var = do_it
print(type(some_var))
# do_it()

# prevented by strong-typing
# print("this is cool: " + str(some_var))
# but not so strong... :)
# print(1 + 2.0)
