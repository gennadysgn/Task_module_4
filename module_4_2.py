def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
# Вывод на консоль:
# Я в области видимости функции test_function

# inner_function()  # Ошибка - NameError: name 'inner_function' is not defined.
# Вне функции test_function функция inner_function не вызывается.
