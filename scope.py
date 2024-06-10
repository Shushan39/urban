def test_function():
    def inner_function():
        text = "Я в области видимости функции test_function"
        print(text)

    inner_function()


test_function()
