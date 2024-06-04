def divide(first, second):
    a = first
    b = second
    c = 'Ошибка'
    if second == 0:
        return c
    else:
        return a/b


result1 = divide(69, 3 )
result2 = divide(3, 0)
print(result1)
print(result2)
