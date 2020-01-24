def func_count(func):
    func._iteration_count = 0
    def wrapper():
        func._iteration_count += 1
        print(f'Фукция {func.__name__} была вызвана {func._iteration_count} раз(а)')
        return func
    return wrapper