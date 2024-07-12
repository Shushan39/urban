def add_everything_up(a, b):
    try:
        # Проверяем, если оба аргумента a и b являются числами (int или float)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b

        # Проверяем, если оба аргумента a и b являются строками (str)
        elif isinstance(a, str) and isinstance(b, str):
            return a + b  # Выполняем конкатенацию

        else:
            return str(a) + str(b)  # Если типы разные, возвращаем их строковые представления

    except TypeError:
        # Если возникает TypeError при выполнении операции сложения или конкатенации,
        # возвращаем строковое представление аргументов a и b
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
