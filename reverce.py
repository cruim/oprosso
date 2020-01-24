from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap():
        ts = time()
        result = f()
        te = time()
        print(f'func:%r took: %2.4f sec' % (f.__name__,  te-ts))
        return result
    return wrap


_list = list(range(10 ** 10))


# Лучшее решение
@timing
def foo_reverse():
  _list.reverse()


@timing
def foo_reversed():
  list(reversed(_list))


@timing
def foo_slice():
    list(_list[::-1])

foo_reverse()
foo_reversed()
foo_slice()