

nums = [1, 2, 3, 4, 5]


# imperative - what & how - less semantic meaning
# for (int x=0; x<len(nums); x++) {
#     print(nums[x])
# }

# more declarative - more semantic
# for num in nums:
#     print(num)


def double(x):
    print("called double: " + str(x))
    return x * 2

# more imperative
# double_nums = []

# for num in nums:
#     double_nums.append(double(num))

# semantic meaning - transform one list of items into a new list of items
# def my_map(transform_fn, items):

#     # how
#     new_items = []

#     for item in items:
#         # what
#         new_items.append(transform_fn(item))

#     return new_items


# def my_map(transform_fn, items):

#     for item in items:
#         # what
#         print("transform: " + str(item))
#         yield transform_fn(item)
#         print("resume: " + str(item))


# more declarative - a lot of semantic
# double_nums = map(double, nums)
# more declarative
# double_nums = my_map(double, nums)

# print(list(double_nums))

# for num in double_nums:
#     print(num)
#     if num > 5:
#         break

# most Pythonic and it's called a list comprehension
double_nums = [double(x) for x in nums]

# print(nums)
# print(double_nums)


# car1 = (1, "Ford", "Fusion Hybrid", 2018, 45000)
# car2 = (2, "Tesla", "S", 2020, 120000)

# cars = [
#     car1,
#     car2
# ]
