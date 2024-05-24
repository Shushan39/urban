my_dict: dict[str, int] = {'Anna': 2008, 'Vasya': 1975, 'Masha': 2002}
print(my_dict)
print(my_dict['Anna'])
if 'Misha' in my_dict:  # 1 вариант вывода по отсутствующему ключу
    print(my_dict['Misha'])
print(my_dict.get('Misha'))  # 2 вариант вывода по отсутствующему ключу
print(my_dict)
my_dict['Egor'] = 2000   # можно по одной паре добавить
my_dict['Artem'] = 2001
print(my_dict)
my_dict1 = {'Egor': 2000, 'Artem': 2001}   # можно сразу несколько пар добавить
my_dict.update(my_dict1)
print(my_dict)
a = my_dict.pop('Anna')
print(a)
print(my_dict)

my_set = {1, 'hello', 1, 2.5, 'hello'}
print(my_set)
my_set.add('world')
my_set.add(9)
print(my_set)
my_set.remove(9)
print(my_set)
my_set.pop()  # удалит случайный элемент
print(my_set)


