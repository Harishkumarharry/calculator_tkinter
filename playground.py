def add(*args):
    value = 0
    for n in args:
        value += n
    return value


print(add(1, 2, 3, 4))
