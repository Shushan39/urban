def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        func_name = func.__name__  # Получаем имя функции
        results[func_name] = func(int_list)  # Вызываем функцию и сохраняем результат
    return results


print(apply_all_func([6, 20, 15, 9], min, max))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
