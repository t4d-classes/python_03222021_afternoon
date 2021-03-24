

# person = dict(first_name="Bob", last_name="Smith")

person = {
    "first_name": "Bob",
    "last_name": "Smith"
}

print(person["first_name"])

person["age"] = 34

print(person)

del person["age"]

print(person)
