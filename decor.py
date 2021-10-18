def func_decor(func_for_decor):
    def func_wrapper():
        print("код до виконання функції")
        func_for_decor()
        print("функція після виконання функції")
    return func_wrapper()

@func_decor
def standart_function():
    print("Я функція")

