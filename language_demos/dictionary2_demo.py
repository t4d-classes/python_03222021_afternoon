person = {
    "first_name": "Bob",
    "last_name": "Smith"
}

# print(person["age"])

# print(person.get("age"))
# print(person.get("first_name"))

# if "age" not in person:
#     person["age"] = 34
# print(person["age"])

print(person.setdefault("age", 34))

print(person.popitem())

print(person.pop("address", "123 Oak Lane"))

print(person)
