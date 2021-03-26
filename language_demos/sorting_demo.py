from random import randint


def gen_name(size=4):

    return "".join([chr(randint(65, 90)) for _ in range(size)])


random_names = [{"id": randint(1, 1000), "name": gen_name(5)}
                for _ in range(100)]

# random_names.sort(key=lambda x: x["name"])

sorted_random_names = sorted(random_names, key=lambda x: x["name"])

print(random_names)
# print(sorted_random_names)


# random_nums = [randint(1, 1000) for _ in range(100)]

# # random_nums.sort()

# sorted_random_nums = sorted(random_nums)

# print(random_nums)
# print(sorted_random_nums)

print(sorted([(1, 2), (1, 1), (2, 2), (2, 1)]))
