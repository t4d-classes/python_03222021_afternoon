from operator import xor

print(True or False)
print(True and False)
print(not True)
print(xor(True, False))

print("Test" or 2)

# falsy
# 0

print("truthy" if 2 else "falsy")

# ""

print("truthy" if "something" else "falsy")

# False
# None
# []
# ()
