def custom_write(file_name: str, strings: list):
    strings_positions = {}

    # Открываем файл для записи с указанием кодировки utf-8
    f = open(file_name, 'w', encoding='utf-8')

    # Итерируемся по строкам из списка strings
    for idx, string in enumerate(strings, start=1):
        # Получаем текущую позицию в файле (байт, с которого начнется запись строки)
        start_position = f.tell()
        # Записываем строку в файл с добавлением перевода строки
        f.write(string + '\n')
        # Заполняем словарь strings_positions
        strings_positions[(idx, start_position)] = string

    # Закрываем файл вручную
    f.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
