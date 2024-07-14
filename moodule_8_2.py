def personal_sum(numbers):
    """
     Функция подсчитывает сумму чисел в коллекции `numbers`
      и считает количество некорректных данных.
    """
    result = 0
    incorrect_data = 0

    try:
        for num in numbers:
            if isinstance(num, (int, float)):  # Если num является числом (int или float),
                # добавляем его к результату
                result += num
            else:
                print(f'Некорректный тип данных для подсчёта суммы - {num}')
                # Если num не является числом,
                # увеличиваем счетчик некорректных данных
                incorrect_data += 1
    except TypeError:  # Обрабатываем исключение TypeError
        incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    """
     Функция вычисляет среднее арифметическое чисел в коллекции `numbers`
    """

    try:  # Проверяем, является ли numbers списком или кортежом
        if not isinstance(numbers, (list, tuple)):
            print('В numbers записан некорректный тип данных')
            return None

        total_sum, incorrect_data = personal_sum(numbers)

        if len(numbers) == 0:

            return 0

        average = total_sum / len(numbers)
        return average

    except ZeroDivisionError:
        
        return 0


print(personal_sum("1, 2, 3"))  # Выведет сообщение о некорректном типе данных
print(personal_sum(567))  # Выведет сообщение о некорректном типе данных
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
