

def do_it(a, b=5, c=10, *args, **kwargs):
    print(a, b, c, args, kwargs)


do_it(1, 2, 3, 4, 5, 6, first_name="Bob", last_name="Smith")
