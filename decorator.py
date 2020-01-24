from functools import wraps


def repeat(limit=5):
    def _repeat(func):
        func.count = 0
        @wraps(func)
        def inner():
            func.count += 1
            if func.count > limit:
                raise Exception('Превышен лимит вызова функции!')
            print(f'Функция {func.__name__} вызвана {func.count} раз(а)')
            return func()
        return inner
    return _repeat