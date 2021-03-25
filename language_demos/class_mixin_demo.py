import json
import yaml


class JsonMixin:

    def to_json(self):
        return json.dumps(self._items)


class YamlMixin:

    def to_yaml(self):
        return yaml.dump(self._items)


class Parent:

    def __init__(self):
        # single underscore convention means protected
        self._items = []


class Child(Parent, JsonMixin, YamlMixin):

    def __init__(self):
        super().__init__()

    def append(self, name, age):
        self._items.append({"name": name, "age": age})

    def __add__(self, person):
        self._items.append(person)
        return self

    def __iter__(self):
        return iter(self._items)

    def __next__(self):
        return next(self._items)


child = Child()
# child.append("Sri", 35)
# child.append("Kavitha", 33)
# child.append("Hilton", 64)
child += {"name": "Sri", "age": 35}
child += {"name": "Kavitha", "age": 33}
child += {"name": "Hilton", "age": 64}


print(child.to_json())
print(child.to_yaml())

for person in child:
    print(person["name"])
