nums = [1, 2, 3, 4, 5]


# def double(x):
#     return x * 2


double_nums = map(lambda x: x * 2, nums)
even_nums = filter(lambda x: x % 2 == 0, nums)

print(nums, list(double_nums))
print(list(even_nums))

print(max([1, 7, 2, 1, 8, 6]))
print(min([1, 7, 2, 1, 8, 6]))
print(sum([1, 7, 2, 1, 8, 6]))


