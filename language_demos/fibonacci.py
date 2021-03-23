import itertools

# 0 1 1 2 3 5 8 (num_1) 13 (num_2) 21 (next_num)


def fibonacci():

    num_1 = 0
    num_2 = 1

    yield 0, num_1

    while True:

        next_num = num_1 + num_2
        yield num_2, next_num
        num_1 = num_2
        num_2 = next_num


fib_gen = fibonacci()

print(fib_gen)

# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))

for prev_num, num in itertools.islice(fib_gen, 0, 10000):
    # print(num, float(num) / float(prev_num) if prev_num > 0 else "no ratio")
    print(num)
