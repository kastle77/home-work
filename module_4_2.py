def test_function():
    def inner_function():
        print('Я в облости видимости функции test_function')
    inner_function()

test_function()
